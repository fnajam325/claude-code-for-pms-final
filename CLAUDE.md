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


### Earlier findings, 23 to 30 Sept 2026 (full text moved to 05-super-speed/archive.md)
- Four responders (Farlight, Meteor Mite, The Undertow, Vesper) fell from about 10-14 offers a week to 0-1 after 4.2 while the other twelve got more; the aggregate hid it. Cause: a decline and a timeout cost the same and nothing restores the score (the 2019 TODO was never built).
- 17 of the 21 "gone quiet" tickets contradict their own weekly data (still unexplained; delivery failure is a hypothesis); 8 of 9 "vanished too fast" tickets are the intended 90s to 60s cut, a decision for Helen.
- 30 Sept correction: acceptance rate does not predict who collapses (Meteor Mite had the lowest); geography is the likely trigger. Ashgrove and Halfmoon show a milder decline. Detail: `02-super-hearing/console-feedback-synthesis.md`.

### Code walkthrough and hypotheses (5 Oct 2026)
- Code path, plain terms: `availability.py` finds who's free → `routing.py` ranks them (closeness 60%, recent yes-rate 25%, skill match 15% post-4.2) → `offer.py` buzzes one at a time down the list until someone says yes → `history.py` keeps the yes-rate score → `config.py` holds the dials.
- Points come off in exactly one place: `record_declined()` in `history.py` (−0.12), used for both active declines and timeouts. Points go back on in exactly one place: `record_accepted()` (+0.08). No decay, no recovery, no other path. A responder who drops to the floor can only climb by being offered jobs, which a low score prevents.
- Anyone more than 45 minutes away gets a flat zero on proximity (`PROXIMITY_HORIZON_MINUTES`), so distance behaves like a cliff, not a slope.
- SUPERSEDED in part (22 Oct 2026: the Rook database now holds each responder's home area and every offer's outcome; there is still no travel-time data; see 05-super-speed/session-log.md): There is no location or travel-time data anywhere in the repo. `travel_time_minutes()` is a stub. The only location clue is Kip saying Meteor Mite and The Gale are in the same city, which complicates the pure-distance explanation for Meteor Mite.
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

SUPERSEDED in part (22 Oct 2026: home areas and offer-level outcomes now come from the Rook database; still needed: travel time, time-to-accept, delivery logs, coverage gaps). **Needed from Ravi:** per-responder location/travel time; offer-level outcomes (accept/decline/timeout); time-to-accept and assignment times; coverage-gap counts. **Ask Helen/Marcus:** why 60s, what success looked like for the routing change, and whether Availability Confidence slipped.

### Brief and prototype for Helen (22 Oct 2026)
- The brief is v4: `05-super-speed/helen-brief-v4.md` plus `helen-brief-v4-reference.md`. Two fixes (a handler card, a responder message); the third (a way back) is held until Wen answers. It recommends option C now, B once Wen signs off. I have not yet confirmed that is my own view (see 05-super-speed/session-log.md).
- Clickable prototype v3 of those two fixes: `05-super-speed/quiet-responder-prototype.html` (artifact link is open to anyone with it). Every change and its reason is in `quiet-responder-prototype-changelog.md`.
- Two rounds of simulated user tests (8 then 9 testers). Handlers rest on real interviews or tickets; responders on tickets and offer data only. Treat as hypotheses, not user evidence. Most agreed: "we're looking into why" is a promise nobody owns (13 of 16); the check-in wording blamed the responder; the watch should end only when an offer is taken.
- Checked in the data: a flat 3-day card rule would fire on healthy low-volume responders (before 4.2: The Drift 3 times, The Gale 2, Ironvale 1). Every Farlight offer from 19 to 28 Aug was missed or declined, so "close when an offer arrives" is wrong.
- Open: who "we" is and by when (Helen); whether delivery can be seen (Wen); a rule that scales to each responder (Ravi); a dated leave status. The brief was updated on 27 Oct 2026 to the prototype v3 wording and the new close rule.
- Do not give Meteor Mite a pronoun: no source states one.
