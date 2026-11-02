# Weekly review-checklist log

## 2026-10-12 — reviewed `05-super-speed/helen-brief.md`

First logged run; the brief was last changed 2026-10-08 (baf5672), so it counts as new. No other brief-like document exists in the repo (other markdown is prompt logs, READMEs, synthesis/agenda notes).

**Owner:** Pass — "**Owner:** Faran (Dispatch PM) — driving this plan and reporting back as each item lands." (line 3). Named person.
**Success criteria:** Pass — "How we'll know it worked" has dated, checkable targets: timeout-vs-no logging live "within one week"; "'Vanished too fast' tickets drop by half within four weeks". Caveat: the third bullet ("four confirmed responders stop declining further within two weeks") is shaky, because the data shows their offers collapsing, not declines, and the brief itself says timeouts and no's can't yet be told apart.
**Consistent scope:** Fail — The brief opens as app-friction changes "that don't depend on the open questions" (line 7), but fast-follow item 5 ("A softer timeout penalty and a score bounce-back rule", line 25) changes backend scoring and waits on real timeout data, and the closing "decision for you" on the 60-second timeout (line 29) is a routing-config call. Neither is app friction, and the brief never acknowledges the widening. The "Held for now" items are correctly marked as not being done, so they don't count.
**Problem before fix:** Pass — "The friction we're seeing" (line 9) and "What we don't know yet" (line 14) come before "What we're starting with" (line 18).

3 of 4 passed; the one failure is a small fix: state upfront that scoring/timeout work is a related follow-on outside the app-friction scope, or move it to an explicit "out of scope, tracked separately" line. Also tighten the third success bullet to a metric the data can measure (e.g. weekly offers per responder for the four stop falling).

## 2026-10-19 — nothing to review this week

The only brief-like document, `05-super-speed/helen-brief.md`, has not changed since 2026-10-08 (baf5672), before the last logged run on 2026-10-12, so it was not re-reviewed. The only markdown added since then, `02-super-hearing/4-2-before-and-after.md` (bb338c0, 2026-10-13), is an evidence write-up, not a brief to a stakeholder. No other brief, PRD or one-pager exists in the repo.

## 2026-10-26 — reviewed `05-super-speed/helen-brief-v4.md`

New since the last run: the v1 `helen-brief.md` was removed and v4 added on 2026-10-22 (9aedcc0, 1433293). `helen-brief-v4-reference.md` is its supporting detail page, read for context but not reviewed separately.

**Owner:** Pass — "**Owner:** Faran (Dispatch PM)" (line 3). Named person; open questions in section 7 each carry a named owner too.
**Success criteria:** Pass — "each of the four gets at least 8 offers a week (70% of their level before 4.2) with at least 9 in 10 answered in time, within 4 weeks of release", plus proposed stop lines and who calls and undoes it (section 5, line 58); full table in the reference page.
**Consistent scope:** Pass — Opening scope (line 4) is what handlers and responders see when a responder stops getting jobs, and how they get back, with the 60-second timer explicitly "a later decision". Section 7 only asks what the timer was meant to fix and the Availability Confidence question is marked "a separate conversation", which is correct bounding. Two things to watch: option A (line 50) changes scoring for all 16 responders, wider than "the four", though it is framed as a way back; and line 56 ("We fix delivery and keep 1 and 2") adds a delivery fix the scope line never mentions.
**Problem before fix:** Pass — Section 1 states the problem ("four responders have lost about 70% of their job offers, and nobody told them why") before the decision. Section 4 gives the full problem, but it sits after the two decision/ask tables (sections 2 and 3), so a reader hits asks before the evidence.

4 of 4 passed; fixes are small. Optional tidy-ups: say in the scope line that option A and a possible delivery fix are contingencies, and consider moving section 4 ahead of the asks tables. Separate from the checklist: line 76 uses "he"/"his" for Meteor Mite, which CLAUDE.md says to avoid because no source states a pronoun, and line 78 uses "her" for Wen, whose pronouns the sources also don't state. Reword both neutrally.

## 2026-11-02 — reviewed `05-super-speed/on-leave-prd.md` and `05-super-speed/helen-brief-v4.md`

Both changed since the last logged run (2026-10-26): commit 5f398e7 (2026-10-27) added the On leave PRD and its reference page and updated brief v4 to prototype v3. Reference pages (`*-reference.md`) were read for context, not reviewed separately.

### `on-leave-prd.md` (new)

**Owner:** Pass — "**Owner:** Faran (Dispatch PM)" (line 3); every open question in section 7 also has a named owner and a date.
**Success criteria:** Pass — "**Zero new tickets in 8 weeks after release** that say leave looks like busy or ask for a leave status... Faran measures it, and Nadia tags the tickets" (section 5). Falsifiable. Caveat: the baseline is only 2 tickets in about 10 weeks, so zero in 8 weeks is a weak signal, and it depends on Nadia's tagging, which is still an open question (section 7, last row).
**Consistent scope:** Pass — Scope line 4 limits it to a handler-set dated leave shown as its own state. Everything later stays inside that. Responder-set leave, Supply's record, and routing/card changes appear only under "Not in the first release" (section 3) or as flagged risks (section 6), which is correct bounding.
**Problem before fix:** Pass — Section 1 states the problem ("looks the same as being busy") before the decision, and section 2 gives the evidence (tickets 3035 and 3143) before section 4 describes what to build.

4 of 4 passed; no fixes needed beyond tightening the success target, since 2 tickets in 10 weeks makes "zero" an easy bar.

### `helen-brief-v4.md` (updated 2026-10-27)

**Owner:** Pass — "**Owner:** Faran (Dispatch PM)" (line 3); stop-line owners named in section 5 ("Faran calls it, Marcus undoes it") and each open question carries an owner.
**Success criteria:** Pass — Promises 1 and 2: "zero responders with no offers 7 days after a card was shown"; promise 3: "at least 8 offers a week... with at least 9 in 10 answered in time, within 4 weeks of release", plus proposed stop lines (section 5, last paragraph).
**Consistent scope:** Pass — The scope line (line 4) now names "an interim scoring fix for the four (section 5)", which closes the earlier gap about option A. Still unmentioned: line 57 ("We fix delivery and keep 1 and 2") adds a delivery fix the scope line never names, and option A changes scoring for all 16, wider than "the four" (flagged as a risk in the table).
**Problem before fix:** Pass — Section 1 states the problem before the decision ("four responders have lost about 70% of their job offers, and nobody told them why"). The full problem is in section 4, after the two asks tables (sections 2 and 3), so a reader meets the asks before the evidence. Unchanged from last run.

4 of 4 passed; fixes are small and optional: name the delivery fix in the scope line, and consider moving section 4 ahead of the asks tables. The pronoun issues noted last run (Meteor Mite, Wen) are fixed.
