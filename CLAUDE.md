# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

_Compiled from everything in `00-rook/company/` (new-hire packet, both one-pagers, release history, Q3 roadmap, glossary, team directory, Priya's handoff, #dispatch-team Slack export of 2 Sept 2026). I'm the new PM for Rook Dispatch, starting Mon 31 Aug 2026 per Marcus. Source docs are dated (roadmap 30 Jun, glossary 4 Aug, team directory 2 Sept)._

### Company
Rook Industries builds coordination and provisioning software for the protective-response sector. Publicly an emergency-services logistics vendor; actual customers are independently operating masked **responders**, plus the **handlers** and **quartermasters** who support them. Rook employs no responders. Founded 2014, 241 people, mostly remote (HQ Site Aleph; Berlin, Singapore, Cornwall). Subscription revenue, priced per active responder. Monthly release train, 4.x numbering.

**Confidentiality is contractual (Security Policy 4.1):** cover identities are never stored. Rook holds capability tags, availability windows and callout history only, with no mapping to a legal identity. Never design anything that assumes we could reconstruct one, and never try to work out who anyone is.

### Products
**Rook Dispatch (mine).** Incident enters the console, Dispatch ranks available responders, the callout offer goes to the top-ranked responder's phone, then accept, or decline/timeout moves it to the next; acceptance assigns the incident and marks the responder engaged.
- Users: handlers (web console: incidents, coverage, routing overrides, availability windows, capability tags); responders (native mobile: accept/decline, set availability).
- Metrics: **acceptance rate** (headline; reported weekly, in aggregate), **time-to-accept** (median seconds), **coverage gap** (no available responder had the required tags).
- Routing config ships with the release, not as a runtime setting handlers can change.
- Releases: 4.0 (7 Apr: new console nav, override audit log); 4.1 (16 Jun: travel-time proximity, bulk callout, push reliability); **4.2 (12 Aug)**: proximity weighted up vs. recent acceptance history, timeout 90s to 60s, console filter persistence, three defect fixes. Console stable; mobile stable since 4.1.

**Rook Supply.** Handler raises a requisition, quartermaster approves, fulfillment is tracked, each item gets a maintenance schedule from its service interval, and field failure reports can pull maintenance forward. **One-way dependency:** Supply *reads* the Responder Availability Record (written by Dispatch) to schedule maintenance into low-callout windows. Any change to how Dispatch computes it hits Supply with no change on their side, so flag it to Supply's PM (not named in the docs) before touching it.

### Vocabulary (the distinctions that matter)
- **Callout** = request for a responder to attend an incident (Dispatch's unit of work). **Callout offer** = that callout presented to one responder. **Callout timeout** = how long an offer stays live (60s now; same for everyone, set per release).
- **Decline** (active refusal) and **timeout** are distinct in the data; both send the callout onward and both lower the recent-acceptance component of **routing priority** (inputs: travel-time proximity, current availability, capability match, recent acceptance history) until it recovers.
- **Coverage gap** is not low acceptance: a gap means nobody *could* go; low acceptance means nobody *would*.
- **Capability tags:** flight, structural-entry, hazmat-tolerant, cold-weather, aquatic, crowd-management, de-escalation.
- **Mutual aid** / "shared cover": responders in different regions covering for each other. Not supported; Q4 exploration.
- Supply terms: **requisition**, **field failure report**, **service interval**.

### People
- **Helen Achebe**: Director of Product (Dispatch & Supply), my boss; owns roadmap and commitments. Chicago.
- **Marcus Oyelaran**: Eng Manager, Dispatch. First call for anything uncertain; can pull rough numbers, not the real weekly ones. Chicago.
- **Wen Li**: Staff Engineer; built the routing/ranking logic and is the only source of truth on it (no written spec). Berlin. Was on PTO 14-24 Aug.
- **Sofia Marino**: Product Designer, console + phone app. Chicago.
- **Nadia Hoffmann**: Support Lead, Dispatch & Supply; sees complaint volume first, worth a standing 15 min. Berlin.
- **Ravi Menon**: Data Analyst, both surfaces; owns the real weekly "how often responders answer" numbers; requests via #data. Singapore.
- **Priya Raghunathan**: predecessor, sole Dispatch PM for 14 months, left 21 Aug. Handoff doc: `00-rook/company/notes/handoff-from-priya.docx`.

### Where things stand (as of the 2 Sept Slack export)
- Since 4.2, callout tickets run ~3x normal. Split is steady at roughly two-thirds "phone never goes off" (unexplained) to one-third "gone before I could answer" (explained by the shorter timeout). A handler emailed Nadia directly, which "never happens".
- **Competing explanations, none verified.** Priya's read: mostly seasonal (August is always soft) plus the timeout cut, and not worth reverting a change responders asked for. But two changes shipped together, and she admits she "made calls faster than I checked them". Treat her read as a hypothesis, and check it against Ravi's real numbers.
- **Unanswered:** Marcus asked on 14 Aug whether the new weights were meant to apply to responders who've been declining, or whether it "just fell out that way" ("the config doesn't distinguish"). Wen was out and the export shows no answer.
- The team deliberately held conclusions until I'd had a week; a regroup on "the 4.2 picture" is due. Nadia has the ticket breakdown ready.
- **Roadmap vs. reality (Q3 roadmap, revised 30 June):** committed for 4.2 were the routing change, **Availability Confidence** (confidence score beside stated availability; driver: support escalations) and timeout tuning. The 4.2 release notes list the first and third but not Availability Confidence. Notes don't list deferrals, so it's unconfirmed, but it looks like it slipped. Priya flags that some Q3 items were squeezed out of 4.2 and **nobody has confirmed with Helen which are still committed**; do that first. Other items: Supply 4.3 requisition approval chains (committed); Q4 exploring: handler phone app (Supply), shared cover (Dispatch). Committed items are locked and change only through Product.
- **Gap to close:** there's no written description of how routing decides who gets pinged. Priya asks me to write it, with Wen.
- Console filter persistence will generate cosmetic tickets; low priority.


### What I found digging into code + data (23 Sept 2026)
- The "mostly seasonal" read doesn't hold up against `00-rook/data/callout-history.csv`: acceptance rate steps down sharply the week 4.2 shipped, not a gradual seasonal slope, and split by responder it's not a broad softening at all — **Farlight, Meteor Mite, The Undertow, and Vesper** collapse from ~10-14 offers/week to 0-1 by end of August while the other twelve responders get *more* offers than before. The aggregate number hides this.
- Likely mechanism, confirmed in `00-rook/code/dispatch-routing/`: `history.py` penalizes a decline and a timeout identically (0.12 vs. 0.08 credit for accepting — `config.py`), and a 2019 TODO to let the score recover over time was never built. Combined with proximity weight going to 0.60 in 4.2, this reads like a floor with no way back for anyone slightly far who takes a couple of declines/timeouts. This is the literal answer to Marcus's unanswered Slack question from 14 Aug about whether the config treats chronic decliners differently — it doesn't.
- The Q3 roadmap's "Availability Confidence — committed for 4.2" never actually shipped (not in release notes, changelog, or code) — this is the exact stale-roadmap conversation Priya flagged as needing to happen with Helen.
- Sofia's console-redesign interviews (`00-rook/feedback/interviews/`) independently corroborate the same pattern (Kip on Meteor Mite vs. The Gale; Aunt Dot on Vesper) — that research is siloed from the support/data side of this investigation and nobody's connected it yet.
- The other nine "gone quiet" tickets (Ashgrove, Nightwell, Ironvale, Halfmoon, The Longcast, Falkirk, Stormwrack, Cindermark, The Drift) don't match their own weekly data, which is flat or rising — can't tell yet if that's anxiety/contagion or just missing event-level granularity.
- Next: got Ravi's real per-responder numbers and the recent-acceptance score itself (not just offer counts) before drawing conclusions with Helen; separately get 20 min with Wen on the decline/timeout scoring. Holding off on touching the 4.2 weights until then — the indicated fix is probably adding score recovery, not reverting the release.
- Sofia's four console-redesign interviews independently corroborate this: 3 of 4 handlers volunteered a "callout vanished too fast" complaint *unprompted*, in a call that wasn't about routing at all — see `02-super-hearing/console-feedback-synthesis.md` for the full breakdown and triage. One-line summary: 4.2's trouble is that it quietly locked a handful of responders out of the rotation almost entirely, while making everyone else's offers vanish faster than they can react — same routing change, two symptoms.

### Ticket deep-dive (28 Sept 2026) — the "gone quiet" story splits in two
- Cross-checking all 25 support tickets against the real weekly data: only 4 of the 21 "gone quiet" tickets actually match a confirmed collapse (Farlight, The Undertow). The other 17, from 9 different named responders (Ashgrove, Nightwell, Ironvale, Halfmoon, The Longcast, Sgt. Falkirk, Stormwrack, Cindermark, The Drift), contradict their own data — this is a **separate, still-unexplained problem**, not covered by the routing fix already in progress. Five of those tickets independently use self-doubting language ("is this thing broken," "is it just me") that never appears in any interview.
- New hypothesis worth testing before assuming it's contagion: a **push-notification or console-display delivery failure** — offers going out and counting normally in the backend but never surfacing to the responder/handler. 4.1's release notes already list push delivery reliability as prior known problem territory. Worth asking Marcus/Ravi for delivery success rates on these nine specifically.
- The timeout complaints (8 of 9 "vanished too fast" tickets) turned out to be the *understood, expected* cost of the intentional 90s→60s cut hitting busy/normal-volume responders more often — this is a policy decision for Helen (keep 60s or dial back), not an open mystery.
- Halloran's requisition complaint (11-day wait on cracked safety gear) never generated a single ticket, while a moderately quiet week generated several — a real reminder that ticket volume alone can't be trusted as a severity signal anywhere in this investigation.
- Full breakdown, priority table, and all the cuts (confirmed vs. unconfirmed, filing-date pattern, handler-vs-self-filed corroboration, repeat filers) are in `02-super-hearing/console-feedback-synthesis.md`.

### Root-cause deep dive (30 Sept 2026) — the theory got corrected, and the scope may have grown
- Ran a 5-agent investigation into root cause using only `callout-history.csv` and the routing code. They agreed the collapse is real, release-triggered, structural (not random/rotating), and not explained by a simple "popular responders get more popular" effect — but they corrected two things I had wrong and found one new thing.
- **Correction:** my working theory that all four collapsing responders had "strong acceptance histories compensating for distance" doesn't hold — Meteor Mite actually had the *worst* acceptance rate on the entire roster, not a good one. Acceptance rate doesn't predict who collapses at all (weak, wrong-signed correlation across all 16). The real discriminator is most likely pure geography/proximity, which we don't have data for — that's now the single most important missing input, more than anything else on the list.
- **Scope may be 6, not 4.** Corporal Ashgrove and Halfmoon show the same steady, never-bouncing-back decline shape the confirmed four showed in their first two weeks — just a few weeks earlier in the curve (down 18-20%, not yet to zero). Worth watching closely rather than writing off as part of the "9 unconfirmed" group.
- Two mechanisms, not one, stacked: the proximity-weight jump appears to cause the *initial* drop in offers (a responder's score isn't at floor yet when their volume first falls); the broken accept/decline scoring with no recovery function is what makes it *permanent* afterward.
- Also confirmed: the aggregate acceptance-rate "recovery" (0.54→0.73) is partly illusory — raw sent and taken counts are both still below the pre-4.2 baseline at 08-31. The rate climbs mainly because the four/six struggling responders' offers stopped being sent, not because the underlying problem improved. Worth pushing Ravi for total callouts placed per week and the coverage-gap metric, not the rate alone.
- Full agent-by-agent findings, the corrected theory, and the "what's still needed" list (location/travel-time data is the top ask) are in `02-super-hearing/console-feedback-synthesis.md`.

### Code walkthrough and hypotheses (5 Oct 2026)
- Code path, plain terms: `availability.py` finds who's free → `routing.py` ranks them (closeness 60%, recent yes-rate 25%, skill match 15% post-4.2) → `offer.py` buzzes one at a time down the list until someone says yes → `history.py` keeps the yes-rate score → `config.py` holds the dials.
- Points come off in exactly one place: `record_declined()` in `history.py` (−0.12), used for both active declines and timeouts. Points go back on in exactly one place: `record_accepted()` (+0.08). No decay, no recovery, no other path. A responder who drops to the floor can only climb by being offered jobs, which a low score prevents.
- Anyone more than 45 minutes away gets a flat zero on proximity (`PROXIMITY_HORIZON_MINUTES`), so distance behaves like a cliff, not a slope.
- There is no location or travel-time data anywhere in the repo. `travel_time_minutes()` is a stub. The only location clue is Kip saying Meteor Mite and The Gale are in the same city, which complicates the pure-distance explanation for Meteor Mite.
- The repo has one commit (the initial import), so we cannot diff pre- and post-4.2 code. The "only configs changed" answer rests on `CHANGELOG.md` and inline "was X until 4.2" comments. Needs confirmation from Wen or Marcus against the real commit history.
- Ranked hypotheses are in the synthesis file. Top two: (1) score can't recover, (2) distance is the trigger. Both are testable with data we can actually get.
- Marcus's 14 Aug question (does the change apply only to prior decliners?) is answered in the code and by data (no clean split by pre-4.2 acceptance rate). Replied in the course Slack channel.
- 4.2 vs. roadmap: weights and 60s timeout match what shipped. Availability Confidence (committed for 4.2) has no trace in the code, data, or notes. That's the item to raise with Helen.
- Next: 20 min with Wen (score recovery, location data, real commit history); pull real score history and push-notification delivery logs from Ravi.

### 4.2 problem statements vs. callout data (6 Oct 2026)
Which 4.2 changes addressed which user problem (statements in "I am a ___ trying to ___, but cannot because ___, which makes me feel ___" form), and what `00-rook/data/callout-history.csv` can say. Data: weekly offers sent/taken for 16 responders, 29 Jun to 31 Aug. No location, timestamps, or decline/timeout split. Week of 10 Aug is mixed (4.2 shipped Wed 12 Aug).

| # | 4.2 change | Problem (user: need, blocked by) | Shipped? | Testable here? |
|---|---|---|---|---|
| 1 | Routing weights: proximity 0.45 to 0.60, recent acceptance 0.40 to 0.25 | Wide-geography responder: wants nearby callouts, but a better-acceptance responder 40 min away outranks them. Stated (Priya, release notes). | Yes | Partly |
| 2 | Console filter persistence | Handler: filters reset each session. Stated (Sofia: "asked for forever"). | Yes | No |
| 3-5 | Defect fixes: duplicate push on re-offer; capability tag order; coverage export timezone | Responder / handler trust and clarity. Stated as defects. | Yes | No |
| 6 | Timeout 90s to 60s | Handler: wants incidents assigned fast, but unanswered offers hold 90s. **Why is not documented; my guess.** | Yes | Barely |
| 7 | Availability Confidence (stated vs. likely-to-answer) | Handler: can't tell if "available" means will answer. Driver "support escalations"; problem is my inference. | **No.** Committed on the 30 Jun roadmap, absent from release notes, changelog and routing code (console side not checked). | No |

**Problem 1 (routing):** offers were redistributed heavily, but there is no location data to say the right people gained.
- Weekly totals: acceptance 0.75-0.78 for six weeks, then **0.54** in the 4.2 week (sends flat at 177, takes 132 down to 96), 0.66, 0.67, 0.73. Takes were still 120 vs. ~132 on 31 Aug.
- Farlight, The Undertow, Vesper, Meteor Mite: 49 offers/wk down to 8 (down 79-89% each, 0-1/wk by 31 Aug); their acceptance 0.76 to 0.12. The other 12: 123 up to 153 offers/wk (ten gained 19-49%; Ashgrove and Halfmoon down ~25% and still falling). Total offers only ~6% lower.
- The four weren't poor acceptors before (pre-4.2 rates 0.69-0.82; roster 0.69-0.84, Meteor Mite lowest). It doesn't read as "offers moved away from decliners".
- Net: the change may have recreated problem 1 for different people, the trade Priya warned about.
- The 0.54 to 0.73 "recovery" is partly an artifact: the collapsed responders' offers left the average.

**Problem 6 (timeout):** can't measure the goal (no time-to-accept, assignment time or coverage-gap data). Only the cost side shows: takes fell ~27% in the 4.2 week with sends flat, consistent with offers expiring before responders answer. The weights changed the same day, so the data can't separate the two.

**Needed from Ravi:** per-responder location/travel time; offer-level outcomes (accept/decline/timeout); time-to-accept and assignment times; coverage-gap counts. **Ask Helen/Marcus:** why 60s, what success looked like for the routing change, and whether Availability Confidence slipped.
