# PRD for Helen: an "On leave" status for responders

**Owner:** Faran (Dispatch PM). **Dated:** 27 Oct 2026. **Status:** For your yes. Nothing changes until you say it.
**Scope:** The first release only: a handler sets a dated leave for a responder, and the console shows it as its own state. Not in it: responder-set leave, Supply's record, travel and time zones, recurring time off, a handover trail, any routing change.

## 1. Summary and decision

A handler can mark a responder unavailable, but that looks the same as being busy. Two handlers have asked for a leave status. **Decision:** say yes to taking this on, so Sofia can design it and Marcus can size it.

## 2. The problem, and who has it

When a responder is away on leave, the only way to show it is to set them unavailable. The console shows that the same as a responder who is busy, so a handler cannot tell "away until the 12th" from "on a job". Two handlers asked for a fix, a month apart:

| Ticket | From | Filed | Status |
|---|---|---|---|
| 3035 | Simone Fischer, for Halfmoon | 5 Aug | closed |
| 3143 | Teresa Alvarez, for Ironvale | 6 Sept | open |

How often leave happens is **unknown**: the database holds no leave data, and the tickets cover 29 Jun to 7 Sept.

**Why now:** the same request came in twice and one is still open. The quiet-responder card in the other brief will also make the difference between "away" and "quiet" matter.

## 3. Goals and non-goals

**Goals for the first release:**
- A handler can say "On leave, back [date]".
- The console shows it as its own state, not as busy.
- It ends by itself on the end date.

**Not in the first release** (all later):
- A responder sets their own leave in the app.
- Leave appears in the record Supply reads.
- Routing and the quiet-responder card learn about leave.
- Travel and time-zone handling, recurring time off, and a handover trail.

## 4. What we would build

| # | Requirement | Priority |
|---|---|---|
| 1 | A handler sets "On leave" for a responder with a start date and an end date, ahead of time. The handler can change or end it. | Must have |
| 2 | The console shows it as its own state, for example "On leave, back 12 Sep", different from Busy and from Unavailable. | Must have |
| 3 | It ends by itself on the end date. | Must have |
| 4 | Only the dates are stored, never a reason (Security Policy 4.1). | Must have |

It builds on the existing unavailable status. Routing offers only to responders marked available, so we expect no routing change. Wen confirms this (section 7).

## 5. How we will know it worked

**Zero new tickets in 8 weeks after release** that say leave looks like busy or ask for a leave status. Today there are 2 in about 10 weeks. Faran measures it, and Nadia tags the tickets.

## 6. Risks and dependencies

| Risk | What we do |
|---|---|
| A responder on leave could still look quiet to the quiet-responder card. The first release does not change the card. | Decide the card rule when the card is designed. Check whether it skips unavailable responders. |
| Leave set by mistake means no offers. | Show it clearly and let the handler end it. |
| Leave dates could change the record Supply reads. | Keep the record's shape the same. If that is not possible, tell Supply's PM first. We do not know who that is. |

**Depends on:** Marcus (size and release slot), Sofia (the screens), Wen (how leave sits on unavailable), Security (wording and the no-reason rule), Nadia (tagging tickets).

## 7. Open questions, with owners

| Question | Owner | By |
|---|---|---|
| Does this rank above the quiet-responder work? | Helen | Week 1 |
| How big is it, and which release? | Marcus | Week 1 |
| Does an unavailable responder get no offers today? Can "unavailable" carry dates, and does anything else read it? | Wen | Week 1 |
| Where can the dates live without changing the record Supply reads? | Wen | Week 1 |
| How many leave periods happen? The database has no leave data. | Ravi | Week 1 |
| Who is the Supply PM? | Helen | Week 1 |
| Can leave tickets be tagged so the 8-week count works? | Nadia | Week 1 |

Detail, the ticket text and the assumptions are on the reference page.
