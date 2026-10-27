# Question bank and must-haves

Use this to build the confidence ledger and to pick the next question. ★ marks a blocker: it must be 1 before you can claim 95%. The ledger is kept short on purpose, about 12 to 15 items per deliverable, so that 95% is reachable in roughly 8 to 10 questions.

## Must-haves for every deliverable (8 items)

| # | Item | Typical question (turn it into options) |
|---|---|---|
| 1 ★ | Purpose: what should this make happen? | "What should the reader or viewer do or decide after this?" |
| 2 ★ | Audience and what they already know | "Who is this for, and how much context do they have?" |
| 3 ★ | Source material: what it is based on, and what it must not use | "Which files, data or decisions is this built from? Anything it must not use? Are any of them guesses or simulated?" |
| 4 ★ | Scope: what is in and what is out | "What is the smallest version that does the job? What should I leave out?" |
| 5 ★ | Success: how will you know it worked | "What would make you call this a good result?" For a PRD, a deck's ask or a prototype's test, it must end with a measure, a target and a time. |
| 6 | Shape and home: length, structure, tone, where it lives, who sees it | "How long, in what tone, and is it a private file, a shared link, or sent to someone?" |
| 7 | Constraints: data, policy, deadline, claims to avoid | "Anything I must not say, show or assume?" |
| 8 | Unknowns and owners: what is unsure, and who could answer | "What are you unsure of, and who could answer it?" |

Items 1 to 5 are blockers for all three deliverables. A deliverable-specific item can also be a blocker if it changes what gets built (marked ★ below).

## Prototype: extra must-haves (7 items)

| Item | Question |
|---|---|
| ★ The moment being shown | "Which single situation should the viewer experience?" |
| ★ Scripted walkthrough or free exploration | "Click-through with a story, or free to explore?" |
| Screens and devices | "One screen, or several? Phone, desktop, both?" |
| Real or sample data | "Use real numbers from the sources, or made-up examples?" |
| States and edge cases | "Which paths must work (happy, error, empty)?" |
| What it must not show | "What should be clearly out of the prototype?" |
| How it will be tested or shown | "Who will click it, and what do you want to learn?" |

Build notes: one self-contained page; keep the story controls separate from the product screens; test every branch; check keyboard focus and contrast; say which numbers are real.

## Slide deck: extra must-haves (6 items)

| Item | Question |
|---|---|
| ★ The one ask or decision | "What is the single thing you want the room to agree to?" |
| ★ Length and time | "How many minutes, or how many slides?" |
| Story arc | "Problem, evidence, options, recommendation, or something else?" |
| Evidence per slide | "Which numbers, quotes or charts must appear?" |
| Presenting or reading | "Presented live, or read on its own?" |
| Appendix | "What detail belongs after the main story?" |

Build notes: the title of each slide is its message; the ask appears on slide 1 or 2; put each chart next to the claim it supports; add speaker notes if presented.

## PRD: extra must-haves (5 items)

Success metrics and open questions are already covered by common items 5 and 8, so they are not repeated here.

| Item | Question |
|---|---|
| ★ Who the user is and the problem they have | "Who has this problem, and what does it cost them?" |
| ★ Goals and non-goals | "What are we trying to achieve, and what are we deliberately not doing?" |
| ★ Priority of requirements | "Which parts are must-have for the first release?" |
| Dependencies and teams | "Who else must act or approve?" |
| Rollout and risk | "How is it released, and what could go wrong?" |

Build notes: problem before solution; every requirement traces to the problem; every metric has a number and a time; every open question has a named owner.

## Choosing the next question

1. List the items still below 1.
2. Take the blocker that would change the deliverable most if you were wrong.
3. Turn it into 2 to 4 options with a recommendation first, based on what the sources suggest.
4. If a source already answers it, score it 1 and say so in one line instead of asking.
5. Blockers are always asked one at a time. When only lower-stakes (non-★) items are left, use one batch question (see SKILL.md, section 4).

## Example turn

> Confidence 40% · open: audience, success, scope.
> Who is this for?
> A. Helen, to decide whether to fund the fix (Recommended: her request is in director-request.txt)
> B. The engineering team, to build it
> C. Handlers, to explain the change
> Or tell me in your own words.

## Example batch question

> Confidence 79% · all blockers at 1 · six lower-stakes items still at 0.5.
> My defaults: about one page in the brief's plain style; no leave reason stored; saved as a private file in 05-super-speed/; Marcus sizes it and Sofia mocks it; risk is that a responder on leave looks quiet; open questions go to Helen, Marcus, Wen and Ravi.
> Should I change any of these?
> A. No changes, all fine (Recommended)
> B. Change shape or where it lives
> C. Change constraints or risks
> D. Change owners or open questions

## Play-back template

> **I'll build:** [deliverable] for [audience], so that [purpose].
> **It includes:** [3 to 5 bullets]. **It leaves out:** [2 to 3 bullets].
> **Assumptions unless you object:** [3 to 5 short items].
> Confidence: [n]%. Say go and I'll build it, or tell me what to change.
