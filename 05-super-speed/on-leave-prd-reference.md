# Reference for the "On leave" PRD

Detail behind `on-leave-prd.md`. Dated 27 Oct 2026. Source: the Rook database (`support_tickets`), `00-rook/code/dispatch-routing/availability.py`, the simulated tests of the quiet-responder prototype, and the interview that scoped this PRD.

## The two tickets, as filed
- **3035**, Simone Fischer, about Halfmoon, 5 Aug, closed: "Halfmoon is away on leave for a week. There is no way to show that in the console except setting her unavailable, which looks the same as being busy. A leave status would help."
- **3143**, Teresa Alvarez, about Ironvale, 6 Sept, open: "Ironvale is away on leave for a week. There is no way to show that in the console except setting her unavailable, which looks the same as being busy. A leave status would help."

The two tickets share the same wording. That may mean one template, so they count as two requests, not as two separate discoveries.

## Baseline for the success measure
- The ticket export covers 29 Jun to 7 Sept, about 10 weeks. A search for "leave", "away", "unavailable" and "availability" found these two leave requests; the other matches were about quiet responders, gear due back, handover notes and time zones, not leave.
- 2 requests in about 10 weeks is the baseline. The target is zero new ones in the 8 weeks after release.
- A ticket counts if it says leave looks the same as busy, or asks for a leave status. Nadia would tag them.

## What the code says
`availability.py`:
- `available_for(region, at)` returns "everyone marked available in this region at this moment."
- "Availability is set by the responder or their handler in the app. Nothing in routing changes it."
- The availability record Supply reads is a contract: "If you change the shape of what current_record() returns, tell the Supply team before you ship it."

From this I infer that a responder who is not marked available gets no offers, so leave built on unavailable needs no routing change. That is an inference from a code comment, and Wen needs to confirm it.

## Simulated testing (hypotheses, not real users)
In the second round of simulated tests of the quiet-responder prototype, three testers were built from the same tickets (Simone, Teresa and Ironvale). All three asked for leave to be set ahead with real dates, from Availability and not inside a check-in message. One (Simone) also wanted to know that leave would not count against routing priority or a responder's "usual" volume. Because they were built from these tickets, they add detail, not new evidence.

## Assumptions I made
- The handler can change or end a leave (requirement 1). Otherwise leave could trap a responder.
- Leave is built on the existing unavailable status. This is what lets the first release avoid any routing change.
- No leave reason is stored. Free text could identify someone, and Security Policy 4.1 says cover identities are never stored.
- The example date ("back 12 Sep") is made up, to show the shape of the label.

## What was left out, and why
| Left out | Why |
|---|---|
| A responder sets leave from the app | Decided: later. One place to set it is enough for a first release. |
| Leave in the record Supply reads | Decided: later. It changes a contract and needs Supply's PM, whose name we do not have. |
| Routing and the card treat leave as unavailable | Decided: later. The first release builds on unavailable, so routing already skips it; the card is a separate, unbuilt feature. |
| Travel and time zones, recurring time off, handover trail | Decided: out of scope. Tickets 3050, 3116 (time zones) and 3008, 3068 (handover notes) exist and are separate requests. |

## How this PRD was made
It came from an interview of 9 questions, one at a time, using the `interview-to-build` skill. Seven lower-stakes defaults (shape, constraints, where it lives, dependencies, risks, unknowns, owners) were confirmed in one batch.
