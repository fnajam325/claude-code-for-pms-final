# Quiet Responder prototype: change log

File: `quiet-responder-prototype.html`. Private artifact: https://claude.ai/artifact/PPRL62aqpZuG7UXrTus91w

**How to read the evidence.** Every "why" below comes from a simulated user test on 22 Oct 2026: eight role-played testers (handlers Kip, Dot, Ambrose, Halloran; responders Meteor Mite, Vesper, The Undertow, The Gale) who read a text script of v1, on a mix of Opus, Sonnet and Haiku. The handlers are grounded in the real interview transcripts. The responders are not, because no responder interviews exist, so their reactions are hypotheses. Testers did not click the real page. "n of 8" counts testers who raised the point. Nothing here replaces testing with real handlers and responders.

---

## v3 (22 Oct 2026)

**Evidence for v3.** A second simulated round with nine new testers, none from round 1: four handlers (Linda Pruitt, Simone Fischer, Teresa Alvarez, Renata Kovač), four responders (Farlight, Halfmoon, Ironvale, The Drift) and one screen-reader keyboard audit. They were grounded in each person's real support tickets and weekly offer counts, not interviews, so they are still hypotheses. "n of 8" counts the eight role-played testers; the audit is separate. In my script for step 6b I wrote "Kip" for every handler, so three responders flagged a wrong name. That was my script, not the prototype, and I ignored it. Items marked "checked" were verified by me against the database or code, not just reported by a tester.

| # | Change | Why (evidence) | Status |
|---|---|---|---|
| 1 | **Check-in rewritten:** "Checking in: you haven't had an offer since 22 Aug. Your availability and tags look right from here. Has anything changed on your end?" (still editable). | v2 swapped blame on availability for blame on the phone. 6 of 8 read "Is anything looking wrong on your phone?" as blaming the phone, and 2 more found it too vague (Linda, Simone, Farlight, Halfmoon, Renata, Ironvale, Drift, Teresa). Linda's own draft added the facts. | Done. "Look right from here" must be something Rook can really check. |
| 2 | **Replies reworked:** "Nothing has changed on my end" and "Something looks off". The second asks **what kind** (arrive late, arrive twice, disappear before I can answer, nothing at all), then says an update is coming by "[time to be agreed]". | 4 of 8 said a responder cannot know "everything looks right on my end" (Farlight, Simone, Ironvale, Halfmoon). 5 of 8 said "something looks wrong" led nowhere (Farlight, Ironvale, Linda, Teresa, Halfmoon). Ironvale and Teresa asked for the kind of problem. | Done. The reply window needs an owner. |
| 3 | **Pause removed from the replies.** | 7 of 8 had a problem with it. Linda, Farlight and Halfmoon read it as an opt-out, or a hint to go away, for someone starving for offers. The Drift could mis-tap it, next to the real reply. Simone, Teresa and Ironvale wanted a dated leave status set from Availability, not buried in a "why no offers?" prompt. | Done. A dated "on leave" status is now a separate item. |
| 4 | **The watch ends only when the responder takes an offer.** An offer that goes unanswered leaves "Still watching". The story bar lets you pick "Mite takes the offer" or "The offer goes unanswered". | 5 of 8 said closing on one offer is too early (Linda, Simone, Teresa, Farlight, Halfmoon), on top of 3 in round 1. **Checked:** every Farlight offer from 19 to 28 Aug was missed or declined. Meteor Mite's 27 Aug offer was declined, and Mite took none through 6 Sept. The old rule would have closed those cases on offers nobody answered. | Done. The brief's rule is "until an offer arrives" and needs the same change. |
| 5a | Card text: **"Last offer: 22 Aug, not taken"** (was "no answer in time"). | Teresa and Farlight still read "no answer in time" as fault, or as ambiguous when a phone never rang. "Not taken" is true for every outcome. | Done |
| 5b | Chip: **"Watching 1 responder"** (was "1 responder still quiet"). The word "case" is gone from the interface. | Simone and Renata read "still quiet" as scolding the responder. 4 of 8 found "case" and "open" jargon (Drift, Renata, Ironvale, Halfmoon). | Done |
| 5c | **"Show message"** replaces "Details" on the collapsed banner. | Ironvale, Simone and Farlight asked what "Details" opens. | Done |
| 5d | Help line under the card buttons: "Hide only puts this card away. Kip keeps watching, and the 'Watching' chip stays in the header." | 3 of 8 asked how long it hides and from whom (Renata, Simone, Teresa). | Done |
| 6 | **A quiet pattern line on every card:** Meteor Mite "Last 7 days: 3 offers · usual 11 · down 73%", The Gale "15 offers · usual 13 · up 15%". No alert. | Simone and Halfmoon: a slow decline (11 to 8 a week) never triggers the card. Round 1: The Gale looked calm while carrying more; Ambrose wanted "silence means healthy". **Checked:** the numbers are real, over the 7 days to 25 Aug 21:00; the usual rates are the 6 weeks before 10 Aug. | Done. A threshold alert for slow decline is not built. |
| 7 | **Example moved to Tue 25 Aug, 21:00** (was 9:00). The Gale's "3 offers today" line is gone. | My own correction. **Checked:** Meteor Mite's last offer was 22 Aug at 20:53, so the 3-day mark falls on the evening of 25 Aug, not the morning. The Gale's three offers that day were not all in by 9:00. | Done |
| 8 | Scope line now reads: "Not covered here: offers that vanish too fast. That is the 60-second timer decision, which comes later." | Linda and Renata said offers that vanish is "the same story" for them. The line now says where it is decided. | Done |
| 9 | **Accessibility batch** (from the screen-reader audit, checked by me against the code): unavailable buttons use `aria-disabled` plus a click guard instead of `disabled`; focus moves to the new content after each action; hidden live regions announce the console and phone changes; `aria-expanded` on the chip and the slim banner; labels that name the responder; headings (`h2`, `h3`) instead of bold text; `aria-describedby` on the message box and replies. | The audit found keyboard focus was lost on nearly every action, and changes were not announced. Every button did already have a name, so Yusuf's "button with no name" ticket did not reproduce here. **Tested:** focus never drops to the page body after the first load. | Done |
| 10 | **Contrast fixes:** light-theme green darkened (white text 3.5:1 to about 5.4:1); dark text on green in dark theme (was 1.7:1); a double focus ring that shows on the orange strip (the old orange ring was invisible there); unavailable buttons at 70% opacity with a dashed border; footer text colour raised. | The audit's numbers. **Checked:** I recomputed the contrast ratios myself. | Done. Not tested in a real screen reader. |

### Not changed in v3, and why
| Finding | Evidence | Why not changed |
|---|---|---|
| **"We've told your handler, and we're looking into why."** | 8 of 8 in round 2 (13 of 16 across both rounds). Linda filed 11 tickets that nobody answered. | Needs Helen: a named owner and a date, or drop the line. The page flags it. |
| **The flat 3-day rule fires on healthy low-volume responders.** | **Checked:** in the six weeks before 4.2, The Drift had three gaps of 3+ days, The Gale two and Ironvale one. Farlight and Meteor Mite had none. That is about six of the brief's seven "other twelve" cards from three healthy responders. | A rule that scales to each responder's own gaps needs testing on the pre-4.2 data (Ravi). The page flags it. |
| **Can the card show whether an offer reached the phone?** | 5 of 8 asked (Farlight, Ironvale, Teresa, Linda, Simone), on top of 3 in round 1. | Depends on delivery logs and Wen's open question. Nothing here shows it. |
| **The check-in uses the same push that may be failing.** | Ironvale and Teresa. Ironvale's phone sometimes gets notifications late or not at all. | Needs a decision on a second channel. |
| **A dated "on leave" status** | Simone, Teresa and Ironvale; also existing tickets 3035 and 3143. | Separate item, not part of this check-in. |
| **A handover trail** (who sent, who hid, when) and **travel / time-zone handling** | Teresa (shared computer, night cover); Renata (Stormwrack working from another city). | One tester each. Later. |
| **"Your account is active" line** | Farlight, Linda, Simone. | Rook must be able to say it truthfully. |
| **The brief still has the old wording.** | The v4 brief says "Dismiss", "Last offer missed", the old check-in, and "until they get an offer". | Not changed in this round. Update it if v3 is adopted. |

---

## v2 (22 Oct 2026)

| # | Change | Why (evidence from the test) | Status |
|---|---|---|---|
| 1a | Button **Dismiss** renamed **Hide for now**. | All 4 handlers read "Dismiss" as "handled" (Kip, Dot, Ambrose, Halloran), across both Opus and Sonnet. The card hides but the case stays open, so the word promised something false. | Done |
| 1b | The header chip **"Quiet responders: 1 open"** became **"1 responder still quiet"**, is larger, and is now a button. Clicking it brings the card back, and "Hide for now" puts it away again. | 3 handlers said they would miss the small chip (Kip, Dot, Halloran). Dot and Ambrose found "open" to be jargon: open in what sense? A clickable chip gives a way back to the card. | Done |
| 2 | Card text **"Last offer missed"** became **"Last offer: no answer in time"**, on the card and the alert. | 5 of 8 (Kip, Dot, Ambrose, Mite, Gale) found "missed" ambiguous (declined, timed out or never delivered?) or read it as blame. "No answer in time" is the brief's own definition of missed and does not decide the open question of slowness vs. undelivered. | Done |
| 3a | Check-in text changed from "Is your availability right?" to **"Is anything looking wrong on your phone?"** | 4 of 8 (Kip, Mite, Undertow, Vesper) read the old question as blaming the responder. Kip noted the card already says Available. | Done. Wording is a proposal. |
| 3b | The check-in is now **editable** before sending. The edited text is what the responder sees. | 5 of 8 (Kip, Dot, Ambrose, Mite, Vesper): the template feels like a template, and the responder can tell. Kip and Ambrose asked to edit it. Dot wanted it warmer. | Done |
| 4a | Three replies: **"Everything looks right on my end"**, **"Something looks wrong on my phone"**, **"Pause offers for a week"**. Replaces "My availability is right" and "I'm stepping back". | Both old buttons put the problem on the responder (Vesper). 3 of 4 responders wanted a way to say "my phone isn't buzzing" or to add their own words (Vesper, Mite, Undertow). | Done. Reply wording is a proposal. |
| 4b | "I'm stepping back" removed. **"Pause offers for a week"** adds a **confirm step** ("Pause offers until Tue 1 Sep? You can turn them back on any time.") and shows a "Paused" status. | 6 of 8 said "stepping back" feels like quitting: too final, unclear whether it can be undone or hurts ranking, easy to tap by accident (Kip, Dot, Mite, Vesper, Undertow, Gale). Undertow asked for a middle option such as "pause for a week". | Done. Needs checking against how availability windows work today. |
| 4c | New branch for **"Something looks wrong on my phone"**: the responder sees "Kip has your answer, and the case stays open." The handler sees the reply and the case stays open. A reply alone never closes a case. | Supports the open question of whether missed offers are slowness or non-delivery (Wen). Mite and Vesper said not to ask "is it me?" before checking delivery. | Done as a flow only. Nothing in it checks delivery. |
| 5a | The console now shows **"Waiting for a reply"** after sending. | Kip, Dot and Ambrose asked where the reply comes back to the handler. v1 showed nothing. | Done |
| 5b | The console shows the **responder's reply** in a blue note ("Reply from Meteor Mite: ...") and a plain result note for each branch. | Same as 5a. This also gives the pause branch a visible note for the handler, with no card. | Done |
| 6a | Phone banner restyled from **bright yellow warning** to a **neutral information panel**, with a **"Got it"** button that tucks it into a slim "No offers since 22 Aug · Details" line. | All 4 responders said the yellow banner reads like a warning label or a nag, and cannot be cleared (Mite, Undertow, Vesper, Gale). Brief rule unchanged: a "Got it" only collapses it. It still ends when an offer arrives. | Done |
| 6b | **Scope line** added under the title: "Not covered here: offers that vanish too fast. That is a separate decision." | Ambrose, Vesper and Halloran raised vanishing offers. Ambrose said the team should state plainly that this feature does not address it. | Done |
| 7 | Footer panels updated: "Hiding the card does not close the case... Click the chip to bring the card back"; "No card if... paused offers"; and a new "Still open before this ships" bullet about "we're looking into why". | Keeps the page's own explanation in step with the changes above. | Done |
| 8 | Badge changed to **PROTOTYPE v2**. Typos and pronouns: see below. | Version tracking. | Done |

### Also changed before v2 (v1.1)
- Removed pronouns for Meteor Mite ("his", "himself", "he"). The source material never states any. The page now says "they", "their" or names the responder. Reason: do not infer pronouns the source does not give. Also consistent with CLAUDE.md: never work out who anyone is.

---

## Not changed, and why

| Finding | Evidence | Why it is not in the prototype |
|---|---|---|
| **"We've told your handler, and we're looking into why" is an empty promise.** | 5 of 8: who is "we", and when is the update? Kip guessed correctly that nobody is on it yet. | The wording is the brief's own promise 2. It needs a named owner and a date, or the line should go. This is a decision for Helen, not a prototype fix. The footer now flags it. |
| **Handlers who do not live in the console will not see a main-console card.** | All 4 handlers: Halloran goes straight to a profile; Dot and Kip want a sound or a bigger alert; Ambrose wants "no card" distinguishable from "not checked". | Needs product and design decisions on where the alert lives (profile, push or email, sound). Owners: Marcus and Sofia. Dark mode, per-responder sounds and bigger text are existing console asks. |
| **Step 6b: "no card, no follow-up" splits testers.** | Kip, Ambrose and Halloran were fine with it. Dot and all the responders wanted a real alert and a way back. | The prototype keeps a plain note for the handler plus a "turn back on any time" line for the responder. How loud the alert should be is an open decision. |
| **"Case closed" after one offer.** | Kip, Vesper and Undertow said one offer can be luck. | Brief rule: the case stays open until an offer arrives. How many offers close it is open. |
| **The baseline for "usually 11 a week" after release.** | Ambrose: a rolling baseline would drift down with the problem. | The card uses a fixed first-six-weeks baseline. Whether that holds after release is a decision. |
| **The overloaded side (The Gale).** | 1 tester, and I primed the persona with the numbers. The Gale is about 35% above their pre-4.2 level, yet the card reads as calm. | Check against Ravi's data before adding a promise. The card still shows "3 offers today, usually 13 a week". |
| **Check whether a missed offer reached the phone.** | Mite, Vesper and Undertow said not to ask "is it me?" before checking delivery. Mite asked for a "test my alerts" button. | Depends on delivery logs and Wen's answer to open question 1. |
| **The brief's own wording differs from v2.** | The v4 brief still says "Last offer missed" and "Dismiss" in its section 5 table. | The brief was not changed in this round. Update it if v2 is adopted. |
| Dark mode, alert sound per responder, bigger text, the requisition queue. | Kip, Dot, Ambrose, Halloran | Existing console asks, or Supply. Parked. |

---

## v1 (22 Oct 2026)
First build: one page, a console and a phone, promises 1 and 2. Check-in "Is your availability right?", replies "My availability is right" and "I'm stepping back", the card button "Dismiss", a chip "Quiet responders: 1 open", and a yellow banner.
