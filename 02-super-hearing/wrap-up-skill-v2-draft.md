<!--
DRAFT PROPOSAL, NOT INSTALLED.
This is a proposed upgrade to the course template's .claude/skills/wrap-up/SKILL.md.
Original steps 1 to 6 are kept. New material is marked [NEW].
To use it, copy this file's content (from the --- line below) to .claude/skills/wrap-up/SKILL.md.
-->
---
name: wrap-up
description: Ends a class session in the Claude Code for PMs course. Use it when the student says "wrap up" (or "wrap up this session", "let's wrap up", "end of session", "we're done for today", "I'm done with this module"), or "checkpoint" / "save a checkpoint" in the middle of a session. It saves the prompts the student wrote, writes a session log of what was found and decided, keeps CLAUDE.md short and current, and saves everything to GitHub.
---

# Wrap up

You're closing out a class session for a student in Product School's "Claude Code for PMs" course. They aren't technical, and they typed two words so they wouldn't have to type anything else. Their request is their yes: start right away with one plain sentence such as "Wrapping up today's session now." Don't ask them to type or paste anything unless a step below says to.

**Two modes** [NEW]
- **Wrap up** = the full routine below, at the end of a session.
- **Checkpoint** = steps 3 and 5 only (the session log and the save), with no module changes. Suggest it yourself after a big finding, a corrected earlier claim, or a published deliverable, so detail is not lost if the conversation is later summarised.

## 1. Work out which module this was

(unchanged) The module folders are 01-origin-story (Module 1), 02-super-hearing (Module 2), 03-rewind (Module 3), 04-x-ray-vision (Module 4), 05-super-speed (Module 5) and 06-sidekicks (Module 6). Use the module the work was about; else the first module whose prompts.md still has an empty slot; else ask "Which module was today, 1 to 6?"

## 2. Save the student's own prompts

(unchanged) Write the student's own prompts into that module's prompts.md, one per numbered slot, in order, exactly as typed. Never overwrite or delete anything already there.

**[NEW] Under each saved prompt, add one plain line starting "What it led to:"** with the outcome in under 25 words (a finding, a table, a file, a corrected claim). Never edit the prompt text itself. This turns a list of questions into a record of what each question achieved.

## 3. [NEW] Write the session log

Create or append to `<module folder>/session-log.md`. One dated section per session, with these headings, skipping any that are empty:

1. **Goal**: what the student was trying to do, in one sentence.
2. **Findings**: a table with columns *Finding | Evidence and source | Confidence (observed, estimated, or guess) | Status (confirmed, open)*. Put the actual numbers in. A finding with no source does not go in this table; put it under Open questions instead.
3. **Corrections**: each earlier claim that was overturned or refined: *what we believed, what we found, why*. This is the most valuable section, so never drop it.
4. **Decisions**: what was chosen, by whom, and why, including options that were turned down.
5. **Deliverables**: every file, document, artifact or message produced, with its path or link and who can see it (for example "private artifact", "posted in the team channel").
6. **How to reproduce**: the queries, files and calculations behind the key numbers, short enough to re-run.
7. **Open questions**: each with who could answer it.
8. **Prompts and moves that worked**: reusable phrasings, plus any challenge from the student that changed the analysis.
9. **Start here next time**: the three things to read first.

Rules for the log:
- Record only what was actually established in this session. Do not add new claims or round numbers up.
- Mark estimates and guesses as such. Do not turn a hunch into a fact.
- If a number was later corrected in the same session, record only the final number and list the change under Corrections.

## 4. Update CLAUDE.md, but keep it short [CHANGED]

- Under "## Working context", add three to six short plain lines of what is true now, each ending with a pointer such as "(see 02-super-hearing/session-log.md)". Findings, sources that mattered, questions still open.
- **[NEW] Reconcile before adding.** If a new line contradicts or refines an older line, change the older line to start with "SUPERSEDED:" and say what replaced it. Do not silently delete it.
- **[NEW] Keep it under about 120 lines.** If it grows past that, move the oldest dated sections into `<module folder>/archive.md`, and leave a one-line summary and pointer in CLAUDE.md.
- If the section still holds only the placeholder "_You'll fill this in during Module 1._", replace just that placeholder line.
- Never change anything above the "---" line (the session scope block).
- Rook is fictional. Keep all of this in the course folder: never save it to memory or anywhere outside it.

## 5. Module 5 only: check the build files

(unchanged) If today was Module 5, check that 05-super-speed/brief.md and 05-super-speed/prototype.html are both there. If either is missing, tell the student which one. Don't recreate it.

## 6. Save to GitHub

(unchanged) Follow the "save my work" routine in the course-setup skill (.claude/skills/course-setup/SKILL.md and its references/saving-work.md), with a short message such as "Module 2 wrap-up". Handle every problem exactly the way that routine says. [NEW] Include the session log and any new deliverable files in the save.

## 7. Tell the student

A short checklist, then the link:

✓ Saved your prompts to <module folder>/prompts.md (how many)
✓ [NEW] Wrote the session log: N findings, N corrections, N open questions (<module folder>/session-log.md)
✓ Added what we learned today to CLAUDE.md (and marked N older lines as superseded)
✓ Saved to GitHub: https://github.com/<their username>/claude-code-for-pms-final

**[NEW] Then show the three most important findings in one line each, and add:** "If any of these is wrong, tell me and I'll fix the log." Do not ask them to approve before saving; the correction can come after.

If a step didn't work, mark it ✗ and give the fix in one plain sentence. If saving to GitHub failed, tell them their notes are safe on this computer and what to do next, per the save routine.
