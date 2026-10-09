# Requisition Approval Delays — Root Cause & Prototype

## What I did

1. Searched everything under `00-rook/` for material related to requisitions, approvals, quartermasters, and Halloran's complaint:
   - `00-rook/feedback/interviews/halloran.txt` (the source of the "11-day wait on a cracked vest plate" complaint)
   - `00-rook/feedback/interviews/ambrose.txt`, `kip.txt`, `aunt-dot.txt`
   - `00-rook/feedback/tickets/t-001.txt` through `t-025.txt` (25 support tickets)
   - `00-rook/data/callout-history.csv`
   - `00-rook/code/dispatch-routing/*` (routing, offer, availability, history code)
   - `00-rook/company/supply-one-pager.pdf`, `dispatch-one-pager.pdf`, `roadmap-q3.pdf`, `release-history.pdf`, `about-rook.pdf`, `who-does-what.xlsx`, `glossary.docx`
   - `00-rook/company/notes/handoff-from-priya.docx` and `dispatch-slack-thread.txt`
2. Extracted text from the PDFs (via `pypdf`) and the `.docx` files (via the raw XML, since `python-docx` wasn't installed) since there's no `pdftotext` on this machine.
3. Confirmed which of that material actually bears on requisition approvals versus which is about a different product surface, then built a root-cause narrative from the material that does.
4. Built an HTML prototype (toggle between "current state" and "proposed fix" views of the quartermaster approval queue) and saved it locally instead of publishing it, per the test-run instructions.

## Findings

**Most of the available tickets, interviews, and data are about a different product (Rook Dispatch — callout routing), not Supply.** All 25 tickets, the `callout-history.csv` data, the `dispatch-routing` code, and three of the four interviews (Ambrose, Kip, Aunt Dot) are about callout timing, routing, dark mode, filter persistence, etc. Only Halloran's interview — and only part of it — addresses requisitions. I did not force a connection between the Dispatch material and the Supply complaint; they are genuinely separate systems per the product one-pagers (Supply reads Dispatch's availability record but Dispatch's routing/offer logic has no bearing on Supply's approval chain).

**What the real evidence says about the requisition delay:**

1. **One undifferentiated approval queue.** The Supply one-pager (`supply-one-pager.pdf`) describes the core flow as: handler raises a requisition → it routes to a quartermaster for approval → fulfillment is tracked to delivery. Nothing in that flow tiers requests by urgency.
2. **The priority field is cosmetic.** Halloran, in the 5 Sept 2026 interview: *"There's a priority field. I set it. Doesn't seem to change anything about how fast it actually moves, it just sits in the same queue as somebody ordering a spare set of boot laces."* This is the direct, named cause of the 11-day wait — a cracked vest plate (a safety issue) and boot laces are sorted identically.
3. **No SLA, no escalation.** Nothing in the product surfaces when a request has sat too long, and there's no fallback approver if the assigned quartermaster is slow or unavailable. The request waits on exactly one person with no backstop.
4. **This is already a known, committed gap** — not a surprise finding. `roadmap-q3.pdf` lists "Requisition approval chains" under Rook Supply, target release 4.3, status **Committed**, owner Product. The roadmap item exists; it just doesn't have a concrete scope or failure case attached yet. This investigation supplies that.
5. No Supply-side quartermaster, engineer, or PM is named in `who-does-what.xlsx` beyond Helen Achebe (Director of Product, owns roadmap/commitments) — worth flagging as a gap in itself; there's no clear single owner to hand the 4.3 scope to.

**Root cause, in one line:** Requisition approval has a single flat queue with a non-functional priority flag and no SLA/escalation, so an "urgent" safety item waits exactly as long as a routine one — and in this case, longer, because nothing in the system distinguishes them.

## Prototype

Saved locally at:
`/Users/faran/cc4pm_rook_industries/.claude/skills/root-cause-to-prototype-workspace/iteration-1/eval-1-requisition-prototype/without_skill/outputs/requisition-prototype.html`

It's a single self-contained HTML file (no external dependencies, light/dark aware) with a toggle between two views of the quartermaster approval queue:

- **Current state**: one flat list sorted only by filing date, where "Priority: Urgent" items (the cracked vest plate, a failing comms headset) wait the same or longer than routine ones, because the field doesn't drive ordering.
- **Proposed fix**: the same requests re-sorted into three urgency lanes (Safety-critical / Operational / Routine), each with a visible SLA clock, a "breached" flag when the clock runs out, and automatic escalation to a backup approver for safety-critical items after 24 hours with no action. A root-cause summary panel with source citations is included at the bottom.

**Scope decisions, deliberately kept small:** only the safety-critical lane gets auto-escalation to a backup approver; operational and routine lanes keep the existing single quartermaster signer. This limits the change to the piece that's actually causing harm (urgent safety items stuck for days) without redesigning the whole approval chain or requiring a second approver role everywhere.

If this were a live deliverable rather than a test run, I would have published it as a Claude Artifact (so Halloran, Helen Achebe, and the eventual 4.3 engineering owner could open it directly and comment) instead of a local file, and I would have pointed Helen at the roadmap's existing Q3 "Requisition approval chains" line as the vehicle to carry this scope rather than opening a new work item from scratch.

## Final response delivered to the user

> I dug through the tickets, interviews, and data in `00-rook/`, and here's the thing worth saying up front: almost none of it is actually about Supply. The 25 support tickets, the callout-history data, and three of the four handler interviews (Ambrose, Kip, Aunt Dot) are all about Rook Dispatch — callout routing, dark mode, filter persistence, timing complaints about callouts going to someone else. That's a different product surface. I didn't force a connection; I went looking specifically for requisition/approval material instead.
>
> **Root cause of the 11-day wait, straight from Halloran's own words:** there's one flat requisition queue, no SLA, and the priority field you set doesn't do anything to how fast a request actually moves. Halloran said it plainly: *"it just sits in the same queue as somebody ordering a spare set of boot laces."* A cracked vest plate — a safety issue — and a boot-lace order are sorted identically, by filing date, waiting on a single quartermaster signature with no fallback if that person is slow or unavailable.
>
> The good news: this isn't a mystery you need to go sell internally. It's already on the Q3 2026 roadmap as **"Requisition approval chains" — Supply, target 4.3, status Committed** — it just doesn't have a concrete scope attached yet. This investigation gives you that scope.
>
> **Prototype**: I built a quick before/after mockup of the quartermaster approval queue — toggle between "current state" (flat list, urgent items buried) and "proposed fix" (three urgency lanes — Safety-critical / Operational / Routine — each with a visible SLA clock, a breach flag, and auto-escalation to a backup approver for safety-critical items stuck past 24 hours). I kept the fix narrow on purpose: only the safety-critical lane gets a backup approver, so this doesn't turn into a full approval-chain redesign.
>
> For this test run I saved it as a local file rather than publishing it live: `requisition-prototype.html` in the outputs folder. In the real workflow I'd publish this as a Claude Artifact so you, Halloran, and whoever ends up owning 4.3 can open and comment on it directly, and I'd attach it to the existing "Requisition approval chains" roadmap line rather than opening new work.
>
> One more loose end worth a flag: the team directory doesn't list a named Supply-side quartermaster, engineer, or PM — only Helen Achebe as the roadmap owner. Before 4.3 scoping starts, someone needs to actually own this on the Supply side.
