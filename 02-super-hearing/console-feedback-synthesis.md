# Console + support feedback synthesis

Interactive triage board (interviews): https://claude.ai/artifact/Dt7XNPmeVefB2u6DhAJRvg

Two sources, read together:
- **Interviews** — Sofia Marino's console redesign research, 2–5 Sept 2026, in `00-rook/feedback/interviews/` — Ambrose (handler, Captain Vantage), Dorothy "Aunt Dot" Pell (handler, Vesper), Halloran (handler, Sgt. Bulwark), Kip (handler, Meteor Mite & The Gale).
- **Support tickets** — 25 tickets, 13 Aug – 5 Sept 2026, in `00-rook/feedback/tickets/`.

## The one-sentence read

Based on the interviews, the trouble with 4.2 is that it quietly locked a handful of responders out of the rotation almost entirely, while making everyone else's offers vanish faster than they can react — and it's the same routing change causing both.

A teammate independently framed the same evidence differently: *"the trouble with 4.2 is nobody asked about callouts. Three of the four handlers brought them up anyway."* That's the credibility argument (unprompted, off-topic, and still volunteered by 3 of 4); mine is the mechanism argument (what's actually broken). Worth keeping both — they cover different pieces: the "3 of 4" framing is precise for the vanishing-callout complaint specifically (Ambrose, Dot, Halloran); it doesn't cover Kip's complaint, which is a different symptom of the same root cause (one responder starved of offers entirely, not an offer lost too fast).

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
