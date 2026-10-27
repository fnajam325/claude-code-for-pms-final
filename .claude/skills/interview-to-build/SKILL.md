---
name: interview-to-build
description: Interviews the user, one question at a time, until Claude is about 95% confident what they want, then builds a prototype, slide deck or PRD. Use it when the user says "interview me", "ask me questions until you're confident", "before we build anything, clarify with me", "I want a prototype / deck / PRD / one-pager but I'm not sure how to brief it", or when they ask for a prototype, slide deck or PRD and the request leaves the audience, the purpose or the scope open. Also use it when a first draft missed because the brief was thin. Do not use it for small edits to something that already exists, or when the user has handed over a complete spec.
---

# Interview to build

The goal is to stop guessing. Ask only what the files cannot answer, keep a visible confidence score, and build only when the score is high enough or the user says "go".

## 1. Start by reading, not asking

Before the first question, read what is already there: CLAUDE.md and any files, links or earlier work the user named. Anything you can find, don't ask. Write down what you already know and what it left open. Respect any scope rules in CLAUDE.md (for example, what may be saved where).

Work out the deliverable from the request: **prototype**, **slide deck** or **PRD**. If it is unclear, that is question 1.

## 2. Keep a confidence ledger

Use the must-have list in `references/question-bank.md` for the deliverable (about 12 to 15 items). Each item scores:
- **0**: unknown.
- **0.5**: you proposed a default and the user has not confirmed it, or it is only inferred.
- **1**: the user said it, or a source in the folder states it.

Confidence = total score divided by the number of items, as a percentage. The items marked ★ are blockers: you cannot call it 95% until every ★ is 1, whatever the total. Never round up, and never count your own guess as 1.

**Batch confirmation.** Blockers (★) are always asked one at a time. Lower-stakes items (not ★) that are still at 0.5 because you proposed a default may be confirmed together: list the defaults and ask "Should I change any of these?" with "No changes (Recommended)" first. An explicit "no changes" scores 1 for every default on that list. If they pick a change, ask about that item and keep the rest at 0.5 until they confirm. Say in the confidence line when a batch was used.

Show the running score after each answer, in one line, for example `Confidence 58% · still open: audience, success`. Do not show the whole ledger unless the user asks.

## 3. Ask well

- **One question per message.** Never a list.
- **Offer 2 to 4 options, with your recommendation first and marked (Recommended).** Say in half a sentence why. Let the user answer "other" in their own words. A short reply such as "A" or "a, c" is a full answer.
- Use the AskUserQuestion tool for the options when it is available; otherwise write them as lettered options in the message.
- Ask in order of the most expensive to get wrong: purpose and audience first, look and feel last.
- Do not ask what a file already answers. Do not ask where there is a sensible default; list it as an assumption instead (see section 4).
- Do not lead. If you suspect an answer, offer it as an option among others, not as a question that expects yes.
- If an answer contradicts an earlier one or the sources, say so plainly and ask which holds.
- **If the user declines or leaves out an option you recommended, and it has a consequence** (a risk, a dependency, a gap): say the consequence once, in one sentence, without arguing. Record it as a risk or an open question in the deliverable, and move on. Do not ask again unless a later answer makes it matter more.
- If the user answers something other than what you asked, record it, and ask the same question again only if it still matters.

## 4. Stop interviewing

Stop when any of these is true:
- Confidence is 95% or higher and every ★ is 1.
- The user says "go", "that's enough" or similar. Then state your confidence and which items are still guesses.
- You have asked about 12 questions (a batch counts as one). Say what is still open and ask whether to proceed on stated assumptions.
- Only lower-stakes items are left below 1: use one batch question (section 2), then go to the play-back.

Then do a **play-back**, in under 150 words: what you will build, for whom, what it will and will not include, and a short list of **assumptions you will make unless told otherwise**. End with: "Say go and I'll build it, or tell me what to change." Do not build until they say go. A "yes" to the whole play-back is not a per-item sign-off, so keep assumptions few and clearly labelled.

## 5. Build

Follow the deliverable section in `references/question-bank.md`. In short:

- **Prototype.** One clickable page, built from what was agreed. Use real data from the sources where there is some, and say which examples are real. Test every path in the browser, check for console errors and for sideways scroll at phone width, then show it. Do not publish or save anywhere outside what was agreed. Load any artifact or design skill that is available before writing.
- **Slide deck.** One message per slide, an opening that states the ask, and the evidence on the slide it supports. Use a slides artifact type or the pptx skill if one is available, and ask which the user prefers only if both are.
- **PRD.** Problem before solution, with goals and non-goals, requirements in priority order, success metrics with a target, dependencies, open questions with a named owner. If a spec or docs skill is available, use it for the format.

Whatever you build: mark guesses as guesses, do not invent facts, names, numbers or pronouns, and do not publish, send or push without asking.

## 6. Close the loop

After the first version, give a short table: *what we agreed | where it is in the deliverable | status (built, assumed, not built)*. List every assumption you made and every must-have that ended below 1. Offer one next step, for example a change log, a test round, or a send to a named person.

## Things that go wrong

- Asking three questions at once, so the user answers one.
- Asking what the files say, which costs trust.
- Showing a confidence number that is really a feeling. The ledger exists to stop that.
- Building the first time the score reaches 95%, without a play-back.
- Treating the user's silence on an assumption as agreement on something that matters. Anything that would change the deliverable is a question, not an assumption.
