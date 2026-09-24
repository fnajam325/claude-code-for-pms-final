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

_Compiled from `00-rook/company/` — new hire packet, one-pagers, release history, Q3 roadmap, glossary, team directory, handoff doc, and the #dispatch-team Slack export. I'm PM for Rook Dispatch._

### Company
Rook Industries builds coordination and provisioning software for the protective-response sector. Customers are independently-operating masked responders, plus the handlers and quartermasters who support them — publicly framed as an emergency-services logistics vendor. Founded 2014, ~241 people, mostly remote (HQ at Site Aleph, plus Berlin, Singapore, Cornwall). Subscription revenue priced per active responder. Ships monthly on a 4.x release train.

**Confidentiality — load-bearing, not boilerplate:** responder cover identities are never stored in production. Rook holds capability tags, availability windows, and callout history only — never a mapping to a legal identity. Never design a feature that assumes we could reconstruct one (Security Policy 4.1).

### The two products
**Rook Dispatch** (mine) — responder coordination: availability, proximity, callout routing, acceptance.
- Flow: incident enters console → Dispatch ranks available responders → callout offer goes to the top-ranked responder's mobile → accept, or decline/timeout cascades to the next → acceptance assigns the incident and marks the responder engaged.
- Users: handlers (web console — incidents, coverage, overrides, availability & capability tags), responders (mobile — accept/decline, set availability).
- Metrics: **acceptance rate** (headline, weekly aggregate), **time-to-accept** (median seconds), **coverage gap** (no responder had the required capability tag).
- Routing configuration ships with the release train — not a runtime setting handlers can touch.

**Rook Supply** — gear provisioning: requisition → quartermaster approval → fulfillment → maintenance schedule (from service interval) → field failure reports can pull maintenance forward.
- Users: handlers (requisitions, failure reports), quartermasters (approve, fulfill, own the catalog).
- One-way dependency on Dispatch: Supply *reads* the **Responder Availability Record** (written by Dispatch) to schedule maintenance into low-callout windows. Any change to how Dispatch computes that record flows into Supply automatically — worth flagging to Supply PM when I touch it, since they won't see it coming otherwise.

### Vocabulary
- **Responder / Handler / Quartermaster** — see products above. **Cover identity** — a responder's public persona; no Rook mapping to a legal identity exists.
- **Callout** — a request for a responder to attend an incident. **Callout offer** — that callout presented to one responder. **Callout timeout** — how long an offer stays live (currently 60s, cut from 90s in 4.2). **Decline** vs. **timeout** — distinct in the data, both cascade to the next responder.
- **Routing priority** — the ranking score: travel-time proximity + current availability + capability match + recent acceptance history. Declining/timing out temporarily lowers a responder's own ranking for future callouts.
- **Capability tags** — flight, structural-entry, hazmat-tolerant, cold-weather, aquatic, crowd-management, de-escalation.
- **Mutual aid** — responders in different regions covering for each other. Not built; Q4 exploration.
- **Requisition / Field failure report / Service interval** — Supply-side terms that come up on shared calls.

### People
- **Helen Achebe** — Director of Product, Dispatch & Supply. Owns roadmap and commitments. Chicago.
- **Marcus Oyelaran** — Engineering Manager, Dispatch. Default first call when unsure of anything; can pull rough numbers. Chicago.
- **Wen Li** — Staff Engineer, built the routing/ranking logic. The *only* real source of truth on how ranking works — there's no written spec. Berlin.
- **Sofia Marino** — Product Designer, console + phone app. Chicago.
- **Nadia Hoffmann** — Support Lead, Dispatch & Supply. Sees complaint volume first; worth a standing check-in. Berlin.
- **Ravi Menon** — Data Analyst, shared across both surfaces, owns the real weekly acceptance-rate numbers. Requests go through #data. Singapore.
- **Priya Raghunathan** — my predecessor on Dispatch, solo on the role for 14 months, departed 21 Aug 2026. Left a handoff doc at `00-rook/company/notes/handoff-from-priya.docx`.

### Where things stand (early September 2026)
- Current release is **4.2** (shipped 12 Aug): reweighted routing (proximity up relative to recent acceptance history — a long-requested fix for responders working wide geographies), timeout cut 90s→60s, console filter persistence, three defect fixes.
- Since 4.2, callout-related tickets are running ~3x normal, roughly two-thirds "phone never goes off" (unexplained) and one-third "offer expired before I could respond" (explained by the shorter timeout).
- Priya's handoff take: probably mostly seasonal (August is always soft) plus the timeout change, not the ranking change itself — and she's explicit that relitigating the ranking change just trades one unhappy group of responders for another. Worth verifying against Ravi's real numbers rather than taking on faith.
- The team deliberately held off drawing conclusions until I'd had a week to look myself — a proper regroup on the "4.2 picture" is due now.
- Two open gaps Priya flagged: (1) no written description of how routing decides who gets pinged, only Wen's head — worth writing; (2) some Q3 items got squeezed out of 4.2 and it's unconfirmed with Helen which are still committed.
- **Q3 2026 roadmap** (committed items are locked, changed only through Product): Dispatch 4.2 — done (routing change, Availability Confidence score, timeout tuning). Supply 4.3 — committed (requisition approval chains). Q4, exploring only: handler phone app (Supply), shared cover / mutual aid (Dispatch).

### What I found digging into code + data (23 Sept 2026)
- The "mostly seasonal" read doesn't hold up against `00-rook/data/callout-history.csv`: acceptance rate steps down sharply the week 4.2 shipped, not a gradual seasonal slope, and split by responder it's not a broad softening at all — **Farlight, Meteor Mite, The Undertow, and Vesper** collapse from ~10-14 offers/week to 0-1 by end of August while the other twelve responders get *more* offers than before. The aggregate number hides this.
- Likely mechanism, confirmed in `00-rook/code/dispatch-routing/`: `history.py` penalizes a decline and a timeout identically (0.12 vs. 0.08 credit for accepting — `config.py`), and a 2019 TODO to let the score recover over time was never built. Combined with proximity weight going to 0.60 in 4.2, this reads like a floor with no way back for anyone slightly far who takes a couple of declines/timeouts. This is the literal answer to Marcus's unanswered Slack question from 14 Aug about whether the config treats chronic decliners differently — it doesn't.
- The Q3 roadmap's "Availability Confidence — committed for 4.2" never actually shipped (not in release notes, changelog, or code) — this is the exact stale-roadmap conversation Priya flagged as needing to happen with Helen.
- Sofia's console-redesign interviews (`00-rook/feedback/interviews/`) independently corroborate the same pattern (Kip on Meteor Mite vs. The Gale; Aunt Dot on Vesper) — that research is siloed from the support/data side of this investigation and nobody's connected it yet.
- The other nine "gone quiet" tickets (Ashgrove, Nightwell, Ironvale, Halfmoon, The Longcast, Falkirk, Stormwrack, Cindermark, The Drift) don't match their own weekly data, which is flat or rising — can't tell yet if that's anxiety/contagion or just missing event-level granularity.
- Next: got Ravi's real per-responder numbers and the recent-acceptance score itself (not just offer counts) before drawing conclusions with Helen; separately get 20 min with Wen on the decline/timeout scoring. Holding off on touching the 4.2 weights until then — the indicated fix is probably adding score recovery, not reverting the release.
- Sofia's four console-redesign interviews independently corroborate this: 3 of 4 handlers volunteered a "callout vanished too fast" complaint *unprompted*, in a call that wasn't about routing at all — see `02-super-hearing/console-feedback-synthesis.md` for the full breakdown and triage. One-line summary: 4.2's trouble is that it quietly locked a handful of responders out of the rotation almost entirely, while making everyone else's offers vanish faster than they can react — same routing change, two symptoms.
