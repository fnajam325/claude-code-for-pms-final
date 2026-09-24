# Console feedback synthesis — 4 handler interviews

Interactive triage board: https://claude.ai/artifact/Dt7XNPmeVefB2u6DhAJRvg

Source: interviews conducted by Sofia Marino for console redesign research, 2–5 Sept 2026, in `00-rook/feedback/interviews/` — Ambrose (handler, Captain Vantage), Dorothy "Aunt Dot" Pell (handler, Vesper), Halloran (handler, Sgt. Bulwark), Kip (handler, Meteor Mite & The Gale).

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
