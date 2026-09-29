# Console + support feedback synthesis

Interactive triage board (interviews): https://claude.ai/artifact/Dt7XNPmeVefB2u6DhAJRvg

Two sources, read together:
- **Interviews** — Sofia Marino's console redesign research, 2–5 Sept 2026, in `00-rook/feedback/interviews/` — Ambrose (handler, Captain Vantage), Dorothy "Aunt Dot" Pell (handler, Vesper), Halloran (handler, Sgt. Bulwark), Kip (handler, Meteor Mite & The Gale).
- **Support tickets** — 25 tickets, 13 Aug – 5 Sept 2026, in `00-rook/feedback/tickets/`.

## Plain-language summary

We talked to 4 people who watch the hero screens for a living. We read 25 notes from people asking for help. We looked at a big spreadsheet of numbers. Then we checked if all three agreed with each other.

**The big problem:** After a software update on August 12th, something broke. 4 heroes — Farlight, Meteor Mite, The Undertow, and Vesper — used to get about 12 jobs a week. Now they get 0 or 1. Every single week it got worse, never better. It's like the computer forgot they exist.

**Why it's happening:** The update changed the rules for who gets picked for a job. It now cares much more about "who is closest" and much less about "who says yes a lot." These 4 heroes used to say yes almost every time — that's actually why they used to get picked, even though they live far away. Now that doesn't count as much, so they stopped getting picked at all. Once a hero stops getting picked, there's no way built into the system to fix itself. It just stays broken.

**The tricky part — a second, different problem:** 9 other heroes also complained about being ignored. But when we checked their real numbers, most of them are actually getting the same or more jobs than before. So something else is going on with them — maybe they're just worried after hearing others complain, or maybe there's a totally different bug, like notifications not popping up on their phones. We don't know yet. That's a new mystery to solve.

**A trick with the numbers:** If you just look at "how often do heroes say yes," it looks like things are getting better. But that's a little bit of a magic trick — the number only looks better because the 4 broken heroes stopped getting offered jobs at all, so they stopped dragging the average down. The real amount of work getting done each week is still lower than before. It didn't actually get better. It just looks that way.

**One more clue — timing:** People started complaining the very next day after the update. But the real numbers didn't actually break for about 5 more days. So some complaints came in super early — even one that started before the update even happened, which means the update can't be the reason for that one at all.

**Bottom line:** There's one real, provable problem (4 heroes locked out, and it's the update's fault), one honest metric that's lying a little bit, and one big unsolved mystery (9 more people who feel ignored for reasons we haven't found yet).

## The one-sentence read

Based on the interviews, the trouble with 4.2 is that it quietly locked a handful of responders out of the rotation almost entirely, while making everyone else's offers vanish faster than they can react — and it's the same routing change causing both.

A teammate independently framed the same evidence differently: *"the trouble with 4.2 is nobody asked about callouts. Three of the four handlers brought them up anyway."* That's the credibility argument (unprompted, off-topic, and still volunteered by 3 of 4); mine is the mechanism argument (what's actually broken). Worth keeping both — they cover different pieces: the "3 of 4" framing is precise for the vanishing-callout complaint specifically (Ambrose, Dot, Halloran); it doesn't cover Kip's complaint, which is a different symptom of the same root cause (one responder starved of offers entirely, not an offer lost too fast).

## Priority table (interviews, tickets, and CSV data together)

| Problem area | Interviews | Tickets | CSV data (`callout-history.csv`) | Severity | Action needed |
|---|---|---|---|---|---|
| **Confirmed responder starvation** (Farlight, Meteor Mite, The Undertow, Vesper) | 1 of 4, indirectly (Kip) | 4 of 25 | **Yes** — 4 of 16 responders (25%) cut from ~12 offers/wk to 0-1, decelerating toward a floor with no bounce-back; see deep-dive below | Critical | **Now — fix** (routing / score-recovery change) |
| **Unexplained "gone quiet" reports** (9 other named responders) | 0 of 4 | 17 of 25 | **No** — these 9 responders' weekly `pings_sent` is flat or rising, contradicting the complaint | Unknown severity, but high distress (5 tickets use self-doubting language) | **Now — investigate** (push-notification-delivery hypothesis) |
| Timeout-driven near-misses on normal/busy responders | 3 of 4 (Ambrose, Dot, Halloran) | 8 of 25 | Yes — sent volume for most responders is *rising* post-4.2 (more offers, same 60s window), mechanically explaining more near-misses | Medium, expected tradeoff | **Now — decide** (keep 60s or dial back) |
| **Aggregate acceptance-rate "recovery" is partly illusory** | — | — | **Yes** — raw sent (165 vs. 172.3 baseline) and taken (120 vs. 132.3) are both still below pre-4.2 levels at 08-31, even though the rate climbed from 0.54 to 0.73; the rate recovers mainly because the four starved responders' offers stopped being sent at all | High — masks a real ongoing coverage shortfall | **Now — reframe the metric** (track total callouts placed and coverage gap, not rate alone) |
| Requisition approvals slow, no visibility | 1 of 4 (Halloran) | 0 of 25 — never escalated | N/A (Supply, not in this dataset) | High (safety gear) | **Now — fix**, and flag the ticket-detection gap |
| Status text/badges too small | 2 of 4 | — | N/A | Medium | Next |
| Notifications don't serve handlers | 2 of 4 | — | N/A | Medium | Next |
| No dark mode | 1 of 4 | — | N/A | Low, loud | Next |
| Filter persistence resets | 1 of 4 | — | N/A | Low | Next |
| Field failure reports vanish | 1 of 4 | — | N/A | Low | Next |
| Capability tag legend hard to find | 1 of 4 | — | N/A | Low | Later |
| Catalog search broken | 1 of 4 | — | N/A | Low | Later |

Four things changed from the last pass: the "starvation" bucket split into a confirmed fix and a separate open investigation once the ticket-to-CSV cross-check showed 17 of 21 "gone quiet" tickets don't match the data; the timeout bucket was demoted from "mystery" to "decision" since most of those tickets are the expected, understood cost of an intentional change; the requisition row carries its own flag, since zero tickets for the most severe complaint in the dataset means "ticket count" can't be trusted as a severity signal anywhere else in this table; and a new CSV-only row was added for the rate-recovery illusion, since neither the interviews nor the tickets could have surfaced it — it only shows up by looking at raw counts instead of the ratio.

## Grouped complaints (10 total, by how many of the 4 raised it)

| Complaint | Raised by | Count |
|---|---|---|
| Callouts vanish before responders can answer | Ambrose, Aunt Dot, Halloran | 3 of 4 |
| Status text/badges too small to read at a glance | Ambrose, Aunt Dot | 2 of 4 |
| Notifications don't serve handlers (no handler-side alert; indistinguishable sounds) | Aunt Dot, Kip | 2 of 4 |
| No dark mode | Kip | 1 of 4 |
| Filter persistence resets without warning | Ambrose | 1 of 4 |
| Capability tag legend hard to find | Ambrose | 1 of 4 |
| Requisition approvals slow, no visibility into why | Halloran | 1 of 4 |
| Field failure reports vanish with no feedback | Halloran | 1 of 4 |
| Equipment catalog search doesn't work | Halloran | 1 of 4 |
| Two responders, wildly different weeks, no explanation on screen | Kip | 1 of 4 |

## Quotes, one per complaint

- **Callouts vanish too fast** — "He comes down the stairs two at a time, and by the time he's actually got a thumb on the screen — it's gone." (Aunt Dot)
- **Text too small** — "At a glance I sometimes cannot tell engaged from available without leaning in." (Ambrose)
- **Notifications don't serve handlers** — "I want the alert sound to be different for each of them... both just go 'bing.'" (Kip)
- **No dark mode** — "It's 11pm... the console is just this wall of white light in the middle of my face. I am begging." (Kip)
- **Filter persistence unreliable** — "I'd rather it warned me the filter had reset than simply reset it." (Ambrose)
- **Capability tag legend hard to find** — "There was one in the spring I had to look up twice before it stuck." (Ambrose)
- **Requisition approvals slow** — "A real crack, not cosmetic — it sat waiting on a quartermaster signature for eleven days." (Halloran)
- **Field failure reports vanish** — "I file a failure report and it goes into a void. I'd like to know it did something." (Halloran)
- **Catalog search doesn't work** — "Typed 'plate,' got forty results, half of them unrelated." (Halloran)
- **Divergent responder patterns, unexplained** — "I'm looking at two cards on the same screen that might as well be two different products." (Kip)

## The one thing worth acting on first

Ambrose/Dot's "vanishing callout" complaint and Kip's "two heroes, two different weeks" observation read as separate issues but are almost certainly the same underlying routing problem, seen from two angles — corroborating evidence for the active 4.2 acceptance-rate investigation (see `CLAUDE.md`), not a new, separate fire.

---

## Support tickets (25 total)

### Grouped

| Group | Count | Description |
|---|---|---|
| Gone quiet — no offers at all | 16 of 25 | Ashgrove, Nightwell, The Undertow, Ironvale, Halfmoon, The Longcast, Stormwrack, Sgt. Falkirk, Farlight, The Drift |
| An offer came and vanished before they could react (standalone) | 4 of 25 | Captain Vantage, Sgt. Falkirk, The Longcast, Cindermark |
| Both at once — quiet for a while, then lost the one offer that finally came | 5 of 25 | Nightwell, The Undertow, Cindermark, The Drift, Ironvale |

### Quotes, one per group

- **Gone quiet** — "Nightwell's asked me twice now if her account is actually active, which it is, I've checked. I don't have a good answer for her at this point." (T-004, Marjorie Sung, Nightwell's handler)
- **Vanished before they could react** — "Almost had it. Literally had my thumb on the screen and it switched to someone else. Not happy." (T-015, Cindermark, responder)
- **Quiet, then lost it** — "First one in weeks and it vanished before i could even swipe. of course" (T-023, The Drift, responder)

### Filing-date pattern

Tickets run at roughly one per day from 13 Aug straight through 5 Sept with no decay — undercutting "seasonal, will recover in September" further than the CSV alone did (Nadia's own Slack read on 26 Aug, "not getting worse, not getting better," holds for the whole window).

The compound "quiet, then lost it" complaint (Group 3) only starts appearing after 24 August — but checked against the real per-responder data, only **one of the five** (The Undertow, T-019) is actually one of the four confirmed-collapsing responders. The other four (Nightwell, Cindermark, The Drift, Ironvale) have flat-or-rising ping volume in the CSV for the same weeks. Read: the compound complaint spread as a narrative pattern over time, not because more people were actually starving — people converged on a similar way of describing frustration the longer it circulated, independent of what their own numbers show.

### Other cuts worth running

- **Handler-filed vs. self-filed (mobile), and who has both.** 9 of 11 named individuals in the tickets have *both* a handler ticket and a responder-filed mobile ticket about the same quiet spell — near-universal two-voice corroboration (though not fully independent — handlers and responders talk to each other). More telling: **Meteor Mite and Vesper, two of the four confirmed-collapsing responders, have zero tickets at all**, from either side. The worst real cases never hit the support queue — we only know about them from Sofia's interviews.
- **Filer-assigned severity doesn't track the real cases.** Only one ticket in the set is marked "High" (T-019, The Undertow, a confirmed case) — the rest of the Medium/Low labels are scattered across both confirmed and mismatched cases with no pattern. Not a reliable triage signal on its own.
- **Explicit historical baseline vs. vague "it's been quiet."** A few tickets cite a specific comparison rather than a feeling: Ashgrove's handler calls him "normally one of our busier responders"; Ironvale's handler says nine days straight "has never happened... not since I've been handling her"; Stormwrack's handler says she "track[s] his week against last year's same week out of habit." Two of those three (Ashgrove, Stormwrack) are in the group whose CSV doesn't support the complaint — worth asking Ravi whether `callout-history.csv` is actually complete for every responder, rather than assuming the data automatically wins over a specific, tenured claim.
- **Repeat filers.** Three handlers escalated with a second ticket on the same responder — Marjorie Sung (Nightwell), Desmond Okafor (The Undertow), Teresa Alvarez (Ironvale) — each showing more resignation or higher stakes than their first. A support-process gap independent of root cause: filed once, got no resolution, came back.
- **Capability tag as a competing explanation, not yet ruled out.** The Undertow (aquatic) and Farlight (crowd-management) both carry niche tags. `WEIGHT_CAPABILITY_MATCH` didn't change in 4.2, so this is a weaker explanation than the routing-weight change, but it's still open — worth a one-line check with Ravi on incident volume by required capability tag, pre/post 4.2.

---

## Why the four confirmed responders have never recovered (CSV deep-dive)

The one number for Helen: **4 of 16 responders (25%) have been cut from ~12 offers a week to 0 or 1, three weeks after the release, with no sign of recovery.** Source: `00-rook/data/callout-history.csv`, comparing each responder's weekly `pings_sent` before and after 12 Aug.

Looking at the shape of the four curves, not just the endpoint, explains why "wait for September" won't fix this on its own:

- **The decline never has a good week.** Farlight 10→3→1→0, Meteor Mite 10→4→2→1, The Undertow 11→4→1→1, Vesper 12→5→2→1 — every week, for all four, independently, it only goes down or holds flat. That's the signature of a score with a hard floor and no way back up, matching the unresolved 2019 TODO in `history.py` about adding score recovery.
- **The drop comes in two stages.** A mild dip the first post-release week (08-10), then a 60–70% cliff the second week (08-17) for all four. That fits a compounding loop: the first week's declines/timeouts erode the recent-acceptance score just enough to fall out of contention under the heavier proximity weight, and once that happens they stop getting offered enough to ever earn it back.
- **These four were not chronically unreliable before 4.2 — the opposite, in three of four cases.** Pre-release acceptance rates: Farlight 0.74, Meteor Mite 0.69, The Undertow 0.78, Vesper 0.82 — Vesper's was one of the best on the whole roster, above the 0.77 group average. This rules out "these are just serial decliners" and instead matches the exact profile 4.2's stated rationale targeted: responders compensating for distance with strong acceptance history. The mechanism is working as redesigned, against a specific kind of responder who has no lever left to compensate with.
- **Even the rare offer they still get isn't landing.** By 08-24 and 08-31, all four are down to 1-2 offers/week, and every one goes unaccepted — consistent with them now only reaching the bottom of a long offer cascade (behind everyone who already declined or timed out), a second compounding effect on top of the ranking one.
- **No shared capability tag, no shared handler.** Undertow is aquatic, Farlight is crowd-management, and the other two are unstated — four different specialties and four different handlers (Linda Pruitt, Kip, Desmond Okafor, Aunt Dot) collapsing on the identical timeline. Weakens the "incident mix for a niche tag dried up" alternative and rules out a single handler or account-level issue.

Also worth flagging separately: the aggregate acceptance rate's "recovery" (0.54 → 0.73 by 08-31) is partly an illusion of composition, not genuine improvement. Both raw counts are still below the pre-4.2 baseline at 08-31 — sent 165 vs. 172.3, taken 120 vs. 132.3 — meaning Dispatch is still placing fewer callouts per week than before the release. The rate climbs mainly because the four collapsing responders' offers (which were dragging the rate down) have simply stopped being sent, not because the underlying problem improved. Worth asking Ravi for total callouts placed per week and the coverage-gap metric directly, not just the rate.

---

## Timing: when people wrote in vs. when the numbers actually moved

**People started writing in immediately.** T-001 is dated 13 Aug — one day after 4.2 shipped (12 Aug). Tickets then arrive at roughly one per day, without a gap, through 5 Sept.

**The numbers moved later, and in two steps.** The aggregate rate takes its first hit the week of 08-10 (0.77 → 0.54) — that week contains the release day. But the four confirmed responders only show a mild dip that first week (10-15%); the real collapse — the 60-70% cliff — doesn't happen until the week of **08-17**, five days after the release.

**Where tickets and data agree — a real lag, and an accurate one.** The two confirmed responders who actually have tickets show the data breaking *before* the complaint, not after. The Undertow's first ticket (T-005, 19 Aug: "one callout since the start of the month") lands inside the week his sent count fell from 11 to 4 (week of 08-17). Farlight's first ticket (T-018, 30 Aug: "almost two weeks without a single callout") backs out to roughly 17-18 Aug as the start of her quiet stretch — exactly when her own cliff happened. For these two, tickets are a lagging but accurate indicator.

**Where they disagree, and it's sharper than a magnitude mismatch.** T-002 (Corporal Ashgrove, filed 14 Aug) says his phone "hasn't gone off in six days" — putting the start of his quiet spell at roughly **8 August, four days before 4.2 even shipped**. That complaint cannot be caused by the release at all, by its own stated timeline, and Ashgrove's own data confirms it: his sent count in the release week is 10, identical to his pre-release baseline. Several of the other mismatched tickets (Nightwell's T-004, 18 Aug: "second week running") back out to similarly early or pre-release start dates, and none of their underlying numbers ever actually drop.

**Read:** the confirmed problem produces complaints that lag the real numbers by about a week — what you'd expect from something people notice after it's been going on a little while. The unconfirmed complaints lead the data, or predate the cause entirely, which looks much more like anxiety/contagion spreading through the roster than an independent, real signal from each person.
