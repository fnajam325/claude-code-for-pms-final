# Console filter-persistence theory — investigation report

## What I did

1. Read all 25 tickets in `00-rook/feedback/tickets/` (t-001 through t-025, dated 13 Aug – 5 Sep 2026).
2. Read all 4 research interviews in `00-rook/feedback/interviews/` (Ambrose, Dot/"Aunt Dot", Halloran, Kip) — these were from a console-redesign research round, so filter persistence came up directly.
3. Read the `dispatch-routing` service source (`00-rook/code/dispatch-routing/`: `config.py`, `routing.py`, `offer.py`, `history.py`, `availability.py`) and its `CHANGELOG.md`, to see what actually shipped and when.
4. Pulled `00-rook/data/callout-history.csv` (weekly offers-sent / offers-taken per responder, 10 weeks, 16 responders) and ran it through a quick Python aggregation to check volume and variance before vs. after the release in question.

## What I concluded

**The filter-persistence theory does not hold up. It's very likely a coincidence of timing, not the cause.**

- Filter persistence shipped in the **4.2 release (12 Aug 2026)**, and every single complaint in the ticket set starts the day after, **13 Aug 2026**. That's the only evidence connecting it to the complaints, and it's purely a date overlap.
- The interview transcripts directly undercut the theory. Ambrose (Captain Vantage's handler) describes the filter-persistence fix as a clear win — "the difference between opening the console and immediately being at work, versus... five minutes of housekeeping." His one gripe is that the saved filter has reverted to default twice after a backend update, which is an annoyance for *him*, not something that would stop a responder from getting or keeping a callout. Kip, Halloran, and Dot don't mention filter persistence at all when asked about console pain points.
- Critically, filter persistence lives in the **console UI**. It cannot touch who gets offered a callout, in what order, or how long they have to answer — that logic lives entirely in the separate `dispatch-routing` service, which the console doesn't write to (per `availability.py`'s own comment: "Nothing in routing changes it").
- The ticket content itself splits cleanly into two patterns that have nothing to do with a UI filter:
  - **Quiet-stretch tickets** (T-002, T-004, T-005, T-008, T-009, T-010, T-013, T-014, T-017, T-018, T-021, T-022, T-024): a responder goes 1–4 weeks with few or no offers, despite being marked available.
  - **Vanished-too-fast tickets** (T-001, T-003, T-006/T-007 mentions, T-011, T-015, T-019, T-020, T-023, T-025): an offer disappears to someone else before the responder can answer, often right after a long quiet stretch.

### The actual cause

The same `4.2` release that shipped filter persistence also shipped two **dispatch-routing** changes, documented in its changelog:

```
## 4.2 — 12 Aug 2026
- Rebalanced ranking weights: proximity up, recent acceptance down.
- Callout offer timeout 90s -> 60s.
- Console filter persistence (not in this service).
```

In `config.py`:
- `WEIGHT_PROXIMITY` went from 0.45 → **0.60**
- `WEIGHT_RECENT_ACCEPTANCE` went from 0.40 → **0.25**
- `OFFER_TIMEOUT_SECONDS` went from 90 → **60**

In `history.py`, a `no_answer` (timeout) is scored exactly the same as an explicit decline — both pull the responder's `recent_acceptance` score down by `DECLINE_PENALTY`. There's also an open `TODO(wen, 2019)` noting the score never decays back toward neutral on its own.

Put together, this is a classic feedback loop:
1. Weighting proximity much more heavily than before means responders who are a bit farther from the action (regardless of reliability) get pushed down the ranked list.
2. Once a responder starts getting fewer offers, each missed/timed-out offer dings their `recent_acceptance` score the same as a decline would.
3. A lower acceptance score pushes them further down the list next time too — the 0.25 weight still counts against them — so the gap compounds week over week instead of correcting itself.
4. Meanwhile the responders who *are* close to the action get offered even more (since proximity now dominates), creating the "one card on fire, one card dead" pattern Kip described.
5. When a long-quiet responder finally does get offered something, the shorter 60s window (down from 90s) is tighter than they're used to and tighter than they're now "in the habit" of reacting to — hence the string of "gone before I even unlocked my phone" tickets, often on the very first offer after a dry spell (T-011, T-019, T-025 are explicit about this: first offer in 10 days / two weeks / a month, lost almost instantly).

### Data check

I aggregated `callout-history.csv` by week. The spread between the busiest and quietest responder's weekly offer count was stable (roughly 6–16, a 10-point range) for all seven weeks before the release, then widened sharply starting the week of **Aug 17** (the first full week after the Aug 12 release):

| Week of | Min offers/responder | Max offers/responder |
|---|---|---|
| Aug 10 | 7 | 16 |
| Aug 17 | 3 | 18 |
| Aug 24 | 1 | 20 |
| Aug 31 | 0 | 21 |

Looking at individuals: Farlight, The Undertow, Vesper, and Meteor Mite each fell from a stable ~10–14 offers/week to 0–4/week within three weeks of the release — and their accept-rate within that same transition week also dropped (e.g., Farlight 10 sent / 4 taken, Vesper 12 sent / 6 taken), consistent with missed/timed-out offers starting to compound. Over the same period, Captain Vantage, Nightwell, The Gale, Stormwrack, and Sgt. Falkirk rose from ~10–14/week to ~15–21/week. This is exactly the divergence the ranking-weight change would produce, and it maps one-to-one onto who filed which kind of ticket.

### Bottom line

The "console filter persistence" fix is not the cause of the complaints. It's a genuine, well-received improvement that happens to have shipped in the same release as two routing-algorithm changes that are. Recommend this gets handed to Wen Li's team (owner of `dispatch-routing`, per the service README) to:
- Reconsider the magnitude of the Aug 12 weight rebalance, or roll it back and re-tune more gradually.
- Stop scoring a timeout (`no_answer`) identically to an explicit decline — a responder who simply didn't see the offer in time shouldn't be penalized the same as one who actively said no.
- Revisit the 60s offer window, especially for responders coming off a long gap, and/or add the score-decay the 2019 TODO already flagged.

## Fix mock-up

Since the real root cause is a backend ranking/timeout issue, not a console UI issue, there's no console "fix" that resolves the actual problem — that's a `dispatch-routing` config and scoring change for engineering. What *is* a legitimate, console-side action here is giving handlers the visibility several of them explicitly asked for and don't currently have (T-008: "she asked if there was a way to see her own history and I had to tell her there isn't"; T-018: Linda wants "something more to tell her than 'I don't know'"). That visibility would also have let the team catch this regression within a week instead of over three weeks of tickets trickling in.

I mocked up an **"Offer Activity" panel** for the responder detail view in the console: a per-responder weekly offers-sent/accepted history with a sparkline and an automatic flag when volume drops (or rises) sharply relative to that responder's own baseline, annotated with any recent release that coincides with the shift. Two example states — one flagged (Farlight, showing the real collapse from the data) and one healthy-but-rising (Captain Vantage) — built as a static HTML mock-up rather than published live.

Saved locally at:
`/Users/faran/cc4pm_rook_industries/.claude/skills/root-cause-to-prototype-workspace/iteration-1/eval-3-filter-persistence/without_skill/outputs/mockup-offer-health-panel.html`

If this were being published for real, I'd publish it as a Claude Artifact (private by default) so the design/product team could open and share the link directly rather than passing around an HTML file — kept it local for this test run's scope.

## My response to the user, as I would actually deliver it

---

I dug through all 25 tickets, the four console-redesign interviews, the dispatch-routing source code, and ten weeks of callout history. **The filter-persistence theory doesn't hold up — I don't think that's the cause.**

Here's why: filter persistence lives entirely in the console UI and literally cannot affect who gets offered a callout or how long they have to respond — that's decided by a separate routing service the console doesn't touch. And in the interviews, the one handler who talks about filter persistence in depth (Ambrose) is happy with it; it's not a complaint. The only thing connecting it to the tickets is that it happened to ship on the same day, 12 Aug, as something else.

That something else is the real cause. The same release quietly rebalanced the routing algorithm's weights (leaning much harder on proximity, less on how reliably someone's been taking callouts) and cut the offer response window from 90 seconds to 60. The data backs this up cleanly: before Aug 12, every responder's weekly offer count was pretty stable and close together. After it, the spread blew wide open — several responders (Farlight, The Undertow, Vesper, Meteor Mite, and a few others) fell to 0–4 offers a week within three weeks, while a handful of others climbed to 17–21 a week. That's your "nothing for ten days" tickets. And there's a nasty feedback loop in the scoring code: a missed/timed-out offer counts exactly the same as someone actively turning a job down, which drags down the very score that determines how often they get asked next — so once someone falls behind, it keeps getting worse. The shorter 60-second window on top of that explains the "it was gone before I even unlocked my phone" tickets, especially the ones where it's the *first* offer after a long dry spell (several tickets say exactly this).

My recommendation: send this to Wen Li's team (they own dispatch-routing) to revisit the Aug 12 weight change and the 60s timeout, and to stop penalizing a timeout the same as a decline. That's the actual fix, and it's a backend change, not a console one.

Separately — several handlers told us directly they have no way to see their responder's own offer history when something feels off, and had to say "I don't know" when asked. That's a real, independent gap, so I mocked up a simple "Offer Activity" panel for the console's responder view (sent/accepted trend + an automatic drop/spike flag) that would've surfaced this exact regression within the first week instead of three. It's saved as a local file for now rather than published — happy to turn it into a shareable artifact if useful.
