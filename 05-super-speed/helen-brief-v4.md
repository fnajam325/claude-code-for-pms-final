# Brief for Helen: no responder should quietly disappear

**Owner:** Faran (Dispatch PM). **Dated:** 22 Oct 2026, updated 27 Oct 2026 to match prototype v3. **Status:** An idea for your OK. Nothing changes until you say yes.
**Scope:** What handlers and responders see when a responder stops getting jobs, how they get back, and an interim scoring fix for the four (section 5). The 60-second timer is a later decision. Missed offers and jobs nobody took appear as context and as stop-line guardrails, not as goals. A clickable prototype of promises 1 and 2 exists (https://claude.ai/artifact/PPRL62aqpZuG7UXrTus91w); it was tested with simulated users, not real ones. Our numbers end 6 Sept.

## 1. Executive overview

Since release 4.2, four responders have lost about 70% of their job offers, and nobody told them why. **Decision:** start design on two fixes (tell the handler, tell the responder), and hold the third (a way back) until Wen answers.

## 2. Decisions we need from Helen

| Decision | When |
|---|---|
| Yes: start design on promises 1 and 2 (the handler card and the responder message, section 5) | Now |
| Name who "we" is in "we're looking into why", and by when. Or drop the line. | Week 1 |
| Pick option A, B or C for the four (section 5) | Week 1 |
| Yes or no on promise 3, the way back | Week 3 |

## 3. Open items and decisions we need from other teams

| Team | We need | By |
|---|---|---|
| **Marcus** | A release slot (and what it bumps), a size, an off switch for promise 3 | Week 1 |
| **Wen** | The answers in section 7 | Week 1 |
| **Supply PM** | Does a change in offers affect gear repairs? | Before promise 3 |
| **Sofia** | Mock the two screens (prototype v3 is the starting point) | Week 2 |
| **Security** | Check the wording (Policy 4.1), including "your availability and tags look right from here" | Week 1 |
| **Nadia** | Answer the 45 open tickets (32 quiet, 13 vanished, as of 7 Sept) and write a script | Now |
| **Ravi** | Refresh the numbers, test a card rule that scales to each responder's own gaps, check stop lines weekly | Week 1 |

## 4. The problem we are solving, and why now

Every offer without a "yes" costs a responder 0.12 points, even a missed one. Only a "yes" gives back 0.08, so a low score may mean fewer offers and no way to climb. That is a guess until Wen confirms. 4.2 also cut the answer time from 90 to 60 seconds and shifted weight from recent yes-rate (0.40 to 0.25) to closeness (0.45 to 0.60), so we cannot say which change caused the rise in missed offers (2% to 18%).

**Why now:** a responder needs about 6 yes in 10 offers to keep their score. The other twelve are down to 6.4 to 7.1, from 7.2 to 8.5. Halfmoon and The Drift are lowest, at 6.4.

## 5. Ideal state and the plan to get there

**Ideal state:** no responder goes quiet without someone being told, and everyone has a way back.

| Promise | Draft text (example: Meteor Mite, as of 25 Aug) |
|---|---|
| **1. Handler card** | "Meteor Mite: no offers in 3 days (usually 11 a week). Last offer: 22 Aug, not taken. [Message responder] [Hide for now]". [Message responder] opens a pre-written check-in the handler can edit: "Checking in: you haven't had an offer since 22 Aug. Your availability and tags look right from here. Has anything changed on your end?" |
| **2. Responder message** | "You haven't had an offer since 22 Aug. We've told your handler, and we're looking into why." The responder can reply "Nothing has changed on my end" or "Something looks off", and say what kind (late, twice, disappearing, nothing at all). |
| **3. A way back (held)** | Cheaper misses, nothing for offers outside the responder's own area (where they usually work), a slow rise. All numbers are guesses. |

The card shows after 3 days with no offers, once a week at most. Hiding it does not end the watch. The watch ends only when the responder takes an offer; an offer nobody answers does not end it (all of Farlight's offers from 19 to 28 Aug were missed or declined). Every card also shows its last 7 days against the usual, with no alert, so a slow decline is visible. On our data (29 Jun to 6 Sept) the card would have fired 10 times for the four, and 7 times across the other twelve. About six of those seven come from three healthy responders (The Drift 3, The Gale 2, Ironvale 1, in the six weeks before 4.2), because a flat 3-day rule is too sensitive at low volume. A rule that scales to each responder's own gaps needs testing (Ravi).

| Help for the four until the release (Helen chooses) | Risk |
|---|---|
| **A.** Change one number for all 16: a miss costs 0.02, not 0.12. Needs Wen's yes and an off-cycle release (Marcus to confirm). | A guess; changes scoring for the twelve who are fine |
| **B.** Marcus's team sets the four scores to neutral once, with Wen's sign-off. No release (Marcus to confirm). | They may fall back; no help if offers never reach them |
| **C.** Wait for the monthly release; ship the card and message first | The four stay quiet about a month |

**We recommend C now, and B once Wen signs off.** We do not recommend A.

If offers never reach Mite's phone, promise 3 is the wrong fix. We fix delivery and keep 1 and 2.

**Success for promises 1 and 2:** zero responders with no offers 7 days after a card was shown (hiding a card does not count as handled). **Success for the way back (promise 3):** each of the four gets at least 8 offers a week (70% of their level before 4.2) with at least 9 in 10 answered in time, within 4 weeks of release. **Stop** (proposed; guardrails, measured from launch day): jobs nobody took up 2 points, the other twelve's yes-rate down 5 points, or time to accept 10% slower. Faran calls it, Marcus undoes it.

## 6. Supporting data

| | Before 4.2 | After 4.2 |
|---|---|---|
| Offers a week, Meteor Mite | 11.1 | 3.8 |
| Offers lost by each of the four | | 66% to 75% |
| Offers missed, all responders | 2% | 18% |
| Jobs nobody took | 5% | 11% |
| Other twelve say yes to | 7.2 to 8.5 in 10 | 6.4 to 7.1 in 10 |

Before is 29 Jun to 11 Aug, after is 12 Aug to 6 Sept (Rook database). Replaying the four's offers with gentler penalties keeps them at 0.88 to 0.98 (today's rules: 0.00). It does not show how someone already at zero would climb back. Detail is on the attached reference page.

## 7. Open questions, with owners

| Question | Owner | By |
|---|---|---|
| Does Mite miss offers because they are slow, or because offers never reach the phone? | Wen | Week 1 |
| Do scores survive a restart? | Wen | Week 1 |
| Was a miss counting like a "no" on purpose? Does Wen's 2019 view still stand? | Wen | Week 1 |
| Can the check-in truthfully say "your availability and tags look right from here"? | Wen | Week 1 |
| What was the 60-second timer meant to fix? | Helen | Week 1 |
| Does promise 1 replace Availability Confidence? We think not. A separate conversation. | Helen | Week 1 |
| Who is the Supply PM? | Helen | Week 1 |
| Can promise 3 ship behind an off switch? | Marcus | Week 1 |
| Do the numbers hold after the refresh? | Ravi | Week 1 |
