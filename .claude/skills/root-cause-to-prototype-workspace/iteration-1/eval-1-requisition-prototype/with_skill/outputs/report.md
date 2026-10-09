# Report: requisition approval delays — root-cause-to-prototype run

## What I did, and why

I followed the `root-cause-to-prototype` skill end to end, but the shape of this investigation ended up very different from the dispatch-routing worked example the skill was built from, and that difference is itself the main finding.

**Phase 0 — confidence gate.** The ask was clear on its face: investigate why requisition approvals are slow (Halloran's 11-day cracked-vest-plate case), find the root cause, build a prototype of the fix. I was confident (~90%+) on all four checkpoints — what's being asked, who it's for, what they want to do with it, my role as investigator-then-builder — so I did not stop to ask a clarifying question and went straight into gathering. In hindsight this was the right call: the uncertainty that showed up later wasn't about the ask, it was about data availability, which is a Phase 2/3 finding, not a Phase 0 one.

**Phase 1 — orient.** Read `CLAUDE.md` (empty course template, nothing to extend), the Rook Supply one-pager, the Q3 roadmap, the team directory (`who-does-what.xlsx`), and the glossary.

**Phase 2 — gather completely.** I listed every source in `00-rook/` before reading: 25 tickets, 4 interviews, 1 data CSV, 5 code files, and 6 company docs. I read or grepped all of them. This is where the key finding surfaced: **almost none of this corpus is about Rook Supply or requisitions.** All 25 tickets, the callout-history.csv, the dispatch-routing code, the Slack thread, and Priya's handoff doc are about a different, unrelated problem (Dispatch callout routing / acceptance-rate drop after release 4.2). Three of the four interviews (Ambrose, Aunt Dot, Kip) never mention requisitions either. The *entire* evidentiary base for the requisition-approval question is:
- One aside inside an interview that was actually about console/dispatch research (Halloran, 5 Sept 2026) — he raises the requisition complaint unprompted, the interviewer redirects him twice, then gives him five minutes at the end.
- The Supply one-pager's process description (no tickets, no timing data).
- One line on the Q3 roadmap: "Requisition approval chains," Supply 4.3, Committed, driver "Internal."
- The glossary's definitions of requisition/quartermaster (no SLA concept).

**Phase 3 — cross-reference on purpose.** I checked Halloran's account against every other source I could find:
- *Does the one-pager's process match his complaint?* Yes — it describes a single routing step ("routes to a quartermaster for approval") with no mention of priority tiers, which matches "one queue, everything in it."
- *Does anything corroborate the timing or the "priority field does nothing" claim?* No independent source does — no other handler, no quartermaster, no requisition data export exists in this project.
- *A genuine disagreement worth flagging*: the one-pager describes approval as **one step** (handler → quartermaster), but the Q3 roadmap item is named "Requisition approval **chains**" (plural) — language that implies product/engineering already know there's more than one hop in the real process. That's a real contradiction between the documented model and the roadmap's own naming, and I can't resolve it with what's in this project.
- *Timing check*: Halloran says he filed "three weeks ago" relative to a 5 Sept interview and that the item "sat... for eleven days" — internally consistent, no red flag there (unlike the worked-example pattern of a complaint's own math predating its blamed cause).

**Phase 4 — show the work.** Every claim below is sourced to a specific file; see the Findings table.

**Phase 5 — hypotheses.** Written and ranked below, deliberately by resolvability rather than narrative appeal.

**Phase 6 — parallelize.** Skipped deliberately. The skill calls for parallel subagents when an investigation splits into genuinely independent angles with enough data behind each to pursue separately. Here there is one data point; spawning agents to "investigate" a single quote from three different angles would have been theater, not independent verification, so I did the (small amount of) synthesis myself instead.

**Phase 7 — simulate before building.** I ran a small, clearly-labeled **SYNTHETIC** sensitivity check (in the prototype itself) showing that a plain FIFO queue plausibly produces an 11-day wait at modest, assumed queue-depth and throughput values. Confidence: **35/100** — it shows the mechanism is *plausible*, not that it's *confirmed*, because none of the inputs (queue depth, quartermaster daily throughput) are real measured data.

**Phase 8 — altitude.** I checked `company/notes/` for a direct-request file (something like a director's brief) before assuming a shape for the output — none exists for Supply (only the Dispatch handoff doc and Slack thread). Since this request came directly from the user with a clear two-part ask (investigate, then build), I'm delivering one response at working altitude rather than drafting a separate exec brief nobody asked for.

**Phase 9 — name the gap.** Done explicitly below, and repeated inside the prototype's footer so it travels with the artifact, not just this chat.

**Phase 10 — prototype.** Triggered: the user explicitly asked for a prototype of the fix. Built a small interactive HTML page for the leading hypothesis (a safety-critical fast lane alongside the existing queue). No real users or other interviews were available to react to it, so I did not fabricate simulated stakeholder feedback — the honest move given n=1 source was to ship the prototype with the evidence gap stated on its face, not to invent a round of "feedback" that would read as more validation than exists.

---

## Findings

| # | Claim | Source | Confirmed by |
|---|---|---|---|
| 1 | Halloran filed a requisition for a cracked vest plate; it waited 11 days on a quartermaster signature | `feedback/interviews/halloran.txt` L24 | Single source — his account only |
| 2 | He set the requisition's priority field; it "doesn't seem to change anything about how fast it actually moves" | `halloran.txt` L28 | Single source; consistent with #3 |
| 3 | The documented Supply flow has one undifferentiated queue: requisition → quartermaster approval, no priority tier described | `company/supply-one-pager.pdf`, "Core flow" + "Users" sections | Corroborates #2, but is a process doc, not usage data |
| 4 | "Requisition approval chains" is already a Committed Supply 4.3 roadmap item, driver "Internal" (not support-escalation-driven) | `company/roadmap-q3.pdf` | Independent of Halloran — product already flagged this area before/regardless of his complaint |
| 5 | The roadmap calls it "chains" (plural) while the one-pager describes a single approval step | `roadmap-q3.pdf` vs. `supply-one-pager.pdf` | Internal contradiction, unresolved — no source explains the discrepancy |
| 6 | No dedicated Supply PM or quartermaster is listed in the team directory; Supply is owned at the director level for roadmap purposes only | `company/who-does-what.xlsx` | Context only, not a cause |
| 7 | No tickets, requisition timestamps, or quartermaster interview exist anywhere in this project | Full-corpus grep across `00-rook/` | Confirms the evidence gap itself |

Rows 1 and 2 have **no confirming second source** — flagged here rather than left to blend in with the better-supported rows above them, per the skill's multi-source-table rule.

---

## Hypotheses (ranked by resolvability, not narrative appeal)

**H1 — No prioritization in the queue**
If requisitions are processed in a single FIFO queue with no priority-based sorting, then a safety-critical item submitted on an ordinary day will wait exactly as long as a low-stakes item ahead of it in submission order, because nothing in the documented flow reads the priority field to reorder the queue.
- Confirms if: the priority field has no effect on sort order/visibility to the quartermaster (matches the one-pager's single-step description and Halloran's account).
- Fails if: a priority-based fast lane exists in the actual implementation and this was a one-off bug/misrouting for Halloran's specific item.
- Data needed: already have it (one-pager + Halloran's account agree).
- Resolvable how soon: **now**, at low confidence (n=1 corroboration).

**H3 — Undocumented multi-step approval chain**
If the real approval process has more hops than the one-pager's single "quartermaster signature" step (the roadmap literally calls it "chains"), then delay is partly structural — multiple sign-offs, not just queue position — because each additional required approver adds wait time independent of urgency.
- Confirms if: a quartermaster interview or workflow config shows 2+ required approval steps for at least some requisition types.
- Fails if: the one-pager's single-step description is accurate and "chains" in the roadmap name refers to something else (e.g., a UI label, not multiple approvers).
- Data needed: one more data pull — a quartermaster interview or the actual workflow configuration.
- Resolvable how soon: **this week**, if someone can get 20 minutes with a quartermaster.

**H2 — Quartermaster capacity/staffing bottleneck**
If there are too few quartermasters relative to requisition volume, then wait times would scale with overall queue depth regardless of item type or priority, because the bottleneck is throughput, not routing logic.
- Confirms if: approval-volume/staffing data shows backlog correlates with total submitted volume, not with item category.
- Fails if: throughput is adequate but flagged/urgent items still wait as long as routine ones (would instead support H1).
- Data needed: a requisition timestamp export and quartermaster staffing numbers — **neither exists in this project.**
- Resolvable how soon: **later**, needs a new data pull outside this corpus.

A fourth candidate considered and NOT elevated to a ranked hypothesis: "the priority field is simply broken (a bug) rather than unimplemented by design." Can't distinguish this from H1 with anything in this corpus — recorded per the skill's guidance not to silently drop a considered explanation, but it has the same resolvability profile as H3 (needs a quartermaster or engineer, not more reading).

---

## The gap — what's still unverified, and who should close it

- **n = 1.** The entire finding rests on one interview aside from one handler, captured as a tangent during an unrelated research call. There is no ticket queue, no requisition timing data, and no second account to corroborate that this is a pattern rather than one bad case. Owner: whoever runs Supply research next should get even 3–4 more handler/quartermaster accounts before treating H1 as confirmed.
- **No quartermaster perspective at all.** Every account in this corpus is from the requester's side. The quartermaster may have context (volume, staffing, a reason the priority field isn't wired up) that changes the picture entirely. Owner: Supply PM or Director (Helen Achebe) — no quartermaster is even listed in the team directory, which is itself worth flagging.
- **The "chains" vs. "one step" contradiction is unresolved**, not explained away.
- **The synthetic sensitivity check in the prototype is illustrative only** (confidence 35/100) — it shows an 11-day wait is plausible under a plain FIFO queue at reasonable assumed volumes, not that it's the mechanism.

---

## What I built, and what I'd publish instead of this local copy

Saved as a local HTML file rather than a live Artifact, per the task's instruction to keep this test run lightweight:
`outputs/requisition-queue-prototype.html`

It's a small interactive mock of the quartermaster's requisition queue with two tabs:
- **Current:** a single FIFO queue, vest plate buried at position 6 with an 11-day wait and no SLA.
- **Proposed:** the same queue with a safety-critical lane that pulls armor/plate/harness/breathing-apparatus items into a 48-hour-target lane, leaving the standard lane's wait times untouched for everything else.
- A **SYNTHETIC-labeled** slider-driven sensitivity check (queue depth × quartermaster throughput → estimated wait, current vs. proposed), with its 35/100 confidence score and what would raise it stated in the UI itself.
- A footer repeating the evidence gap, so it travels with the file if forwarded on its own.

If this were going to a real audience, I would publish it as a Claude Artifact rather than hand over a local file, specifically so it's a live link the PM can drop into Slack or a doc for Halloran, the Supply director, or an engineer to react to directly. I did not take that step here only because the task asked me to keep this run local and lightweight.

I did not run a round of simulated stakeholder feedback on the prototype. With only one real account in hand, inventing "Halloran reacts to this mock" feedback would read as a second confirming data point when it's actually zero — exactly the failure mode the skill warns against. If the user wants that rehearsal step next, I'd do it, but labeled simulated on every mention.

---

## My response to the user, exactly as I'd deliver it

> I dug through everything we have — all 25 tickets, all 4 interviews, the Supply and Dispatch docs, the roadmap, the callout data, the code. Here's the honest headline: **almost none of what we have actually covers requisitions.** The tickets, the usage data, and three of the four interviews are all about a completely different problem (Dispatch callout routing). The entire evidence base for your question is one aside Halloran gave during an unrelated console interview, plus the Supply one-pager's process description.
>
> That's thin, so I want to be upfront about what I can and can't claim:
>
> **What the one data point says, and what backs it up:** Halloran's vest-plate requisition sat 11 days for a quartermaster signature. He set the priority field and says it didn't change anything. That matches the Supply one-pager, which describes exactly one undifferentiated approval step — no priority tier, no fast lane. So the leading explanation is **requisitions all sit in one FIFO queue regardless of urgency, and the priority field is currently cosmetic.**
>
> **One thing worth knowing**: this isn't news to Product — "Requisition approval chains" is already a committed Q3 roadmap item for Supply 4.3. But the roadmap calls it "chains" (plural), while the one-pager describes a single step. I can't tell from what we have whether that's just naming, or whether the real process has more approval hops than documented. That's an open question, not a finding.
>
> **What I don't have**: any second handler account, any quartermaster perspective at all (there isn't even a quartermaster in the team directory), and zero requisition timing data. So treat "no prioritization" as the leading hypothesis, not a confirmed root cause — getting even a short quartermaster conversation would do more to firm this up than anything else I could do with what's in this project right now.
>
> **The prototype**: I built a quick interactive mock of the quartermaster queue — toggle between today's single FIFO lane (vest plate buried behind boot laces, 11-day wait, no SLA) and a proposed safety-critical lane that pulls armor/harness/breathing-apparatus items to the front with a 48-hour target, without touching wait times for routine requests. There's also a small sensitivity slider showing why an 11-day wait is plausible under a plain FIFO queue — labeled clearly as illustrative, not real data.
>
> I saved it locally for this run: `requisition-queue-prototype.html`. In the real workflow I'd publish this as a live link so you can drop it in front of Halloran or whoever owns Supply next and get a reaction to something concrete.
>
> **Before you act on this**: get one conversation with a quartermaster. It's the single highest-leverage thing that would turn this from "plausible theory built on one complaint" into something you can actually commit engineering time against.
