---
name: root-cause-to-prototype
description: Use this skill when investigating what went wrong with a product, feature, or release by pulling together multiple messy sources (support tickets, user interviews, usage or telemetry data, code) into a root-cause finding, then turning the leading hypothesis into a testable prototype. Trigger this whenever the user asks to "figure out what happened," "find the root cause," "why did X break / drop / change," wants to reconcile tickets vs. interviews vs. data that disagree with each other, asks for a synthesis or investigation doc across multiple feedback sources, or wants to go from a confirmed problem to a quick interactive prototype to test a fix. Also use it when the user wants a living project working-context file (like a CLAUDE.md) kept current across sessions investigating the same product, or asks to "keep digging" on an investigation already underway in this project.
---

# Root cause to prototype

A repeatable way to turn scattered, disagreeing feedback into a root cause you can defend, and the root cause into something you can show someone. It was built from a real investigation into a dispatch-routing release in this project, and it generalizes to any product problem with multiple data sources.

## Why this shape, not a simpler one

The instinct when someone asks "what happened?" is to read the loudest source (usually tickets or the most recent complaint) and answer from it. That produces a confident, wrong answer almost every time, because the loudest source is rarely the most representative one. The real signal shows up in the *disagreement* between sources — where the ticket queue says one thing and the usage data says another. This skill exists to force that comparison instead of skipping it.

## The phases

Work through these roughly in order, but loop back when something contradicts an earlier conclusion — that contradiction is usually the point, not noise to smooth over.

0. **Confirm before you start.** This skill triggers expensive work — reading everything, spawning subagents, building prototypes — so before any of that starts, state your confidence (0-100) on four things: what's actually being asked, who you're doing it for and their role or stake in the answer, what they're trying to achieve with it, and what your role is in getting them there (investigator, co-writer, decision-maker, something else). If you're below roughly 95% on any of the four, say so and ask a targeted question rather than guessing and proceeding — a wrong guess here doesn't surface until a lot of work is already spent on the wrong target. This isn't a gate for every small follow-up inside an investigation already underway; it's for the moment the investigation itself is kicked off, and again if the ask visibly shifts (a new stakeholder enters, the goal changes, you're asked to represent someone you haven't been representing). Once confidence is high enough, say so briefly and move on — this is a checkpoint, not a report.

1. **Orient.** Read the product and company context once. If a working-context file already exists for this project (check `CLAUDE.md` or similar), read and extend it rather than re-deriving everything from scratch. If one doesn't exist and the investigation will span multiple sessions, offer to create one.

2. **Gather completely.** Read every ticket, every interview, every data file in scope — not a representative sample. A pattern that only shows up in 2 of 9 cases is invisible if you only read 3. List what sources exist before reading any of them, so you know what "complete" means for this investigation.

3. **Cross-reference on purpose.** For every claim, check it against every other source. Explicitly look for disagreement, not just confirmation. When sources agree, say so briefly. When they don't, that gap is usually the most important finding in the whole investigation — slow down there.

4. **Show the work.** Every number or quote gets its source: a file path and line number, a ticket ID, an interview name. Anyone reading the output should be able to check the math themselves without re-running the investigation. Never report a conclusion you can't point back to a row for.

5. **Write falsifiable hypotheses.** Format each as *if / then / because*, with an explicit condition that would prove it wrong (see `references/hypothesis-format.md`). Rank them by how resolvable they are with data you can actually get, not by how interesting they sound. A hypothesis nobody can test is a guess wearing a lab coat.

6. **Parallelize open questions.** When several independent angles need investigating and subagents are available, split them out rather than working each one serially in your own context. When they report back, synthesize honestly: say where they agree, where they disagree, and where they corrected the original theory. Do not quietly average away a disagreement between agents.

7. **Simulate before building.** Before writing a full spec or shipping a fix, replay real data through the proposed mechanism to see if it actually produces the observed pattern. State a confidence score (0-100) for any model or simulation result, and say plainly what would raise or lower it. If real data for a key input is missing, synthetic data can fill the gap for a sensitivity check — but label it SYNTHETIC in the output itself, not just in your own notes, and never let a synthetic result be read as a finding.

8. **Communicate at the right altitude.** The same underlying findings become different documents for different readers: a detailed synthesis file for yourself and the working team, a plain-language summary for a quick read, a short brief for a decision-maker who wants "what are we doing" not "how we found it." Don't draft the decision-maker brief until you know who's reading it and what they actually asked for — check for a direct-request file (something like a `director-request.txt`) before assuming what they want.

9. **Name the gap.** Every output — a synthesis doc, a brief, a prototype handoff — ends with what's still unverified and who owns getting it. A theory presented without its open questions reads as more settled than it is. That's the easiest way for this kind of work to mislead someone downstream.

10. **Prototype and iterate — but only once there's a reason to build something, not automatically.** Finishing phase 9 is a natural stopping point, not an invitation to start building. Move into this phase only when the user explicitly asks for something built, or when the investigation's own stated purpose from phase 0 was to produce something to build. Otherwise, stop at the ranked hypotheses and the named gap, then ask what they'd like next — don't default to the full output menu either. The real options are usually: an interactive prototype, a one-pager, a PRD, or a slide deck with speaker notes. Offer those as a short list rather than guessing which one fits, since each implies a different amount of work and a different reader. Once it's clear what to build: for a prototype, build a small interactive artifact for the leading hypothesis so people can react to something concrete instead of a paragraph. If real users aren't available, simulated stakeholder feedback is useful as a rehearsal — but say clearly, every time, that it's simulated and not real user research, and don't let a simulated reaction get cited later as if it were one. Apply the improvements that come out of real or simulated feedback, then re-publish.

See `references/playbook.md` for a longer walkthrough of each phase with a worked example, and `references/hypothesis-format.md` for the exact hypothesis template.

## Guardrails (apply throughout, not just at one phase)

- **Re-check the confidence gate if the ask shifts mid-investigation.** A new stakeholder, a changed goal, or a request to speak for someone you haven't been representing all warrant another pass at phase 0, not a silent assumption that the original read still holds.
- **Synthetic is not evidence.** Any invented, simulated, or assumed data gets labeled as such in the artifact or document it appears in, not just mentioned once and forgotten.
- **Confidence scores are mandatory for model output.** Any time you present the result of a simulation, a scoring model, or a projection, give a 0-100 confidence score and name what's missing.
- **Multi-source tables carry a confirmation column.** When summarizing findings across sources in a table, include a column showing which source(s) back each row, and flag rows with no confirming source rather than letting them sit unmarked next to confirmed ones.
- **External sends need a scope check.** Before posting to a real external channel or messaging a real person, confirm the destination and the exact content with the user first — don't assume a general "send it" covers a specific channel or recipient you haven't named together.
