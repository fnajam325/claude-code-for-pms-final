# Playbook: root cause to prototype

A longer walkthrough of each phase in SKILL.md, with the worked example this skill was built from: a dispatch-routing release that quietly locked some users out of a system while making everyone else's experience worse in a different way. Names are illustrative; the pattern is what transfers.

## Contents
- Phase 0: Confirm before you start
- Phase 1: Orient
- Phase 2: Gather completely
- Phase 3: Cross-reference on purpose
- Phase 4: Show the work
- Phase 5: Write falsifiable hypotheses
- Phase 6: Parallelize open questions
- Phase 7: Simulate before building
- Phase 8: Communicate at the right altitude
- Phase 9: Name the gap
- Phase 10: Prototype and iterate
- Worked example, condensed

## Phase 0: Confirm before you start

Before reading a single file, say your confidence on: what's being asked, who it's for, what they want to do with the answer, and what your role is. If any of those is fuzzy, a few minutes of clarifying questions now saves hours of work aimed at the wrong target later. This matters more here than in most skills because the downstream cost of a wrong start is high — full data reads, subagents, prototypes.

Example of a bad silent assumption: treating a request to "find out why engagement dropped" as a request for a root-cause investigation, when the person actually wanted a two-line status update because they're about to walk into a meeting. The confidence check would have caught the mismatch between "what's being asked" (a status update) and "what your role is" (full investigator) before any work started.

## Phase 1: Orient

Look for an existing working-context file before writing one. In a project that already has something like a `CLAUDE.md`, read it fully — it likely has the product model, the people, the vocabulary, and what's already been tried. Extend it rather than duplicating it elsewhere. If this is the first session on a given product, build one: company/product basics, key people and their role in the investigation, vocabulary that'll come up often, and current state. Keep it current as you learn more — a stale working-context file is worse than none, because it gets trusted anyway.

## Phase 2: Gather completely

List every source before reading any of them: every ticket, every interview or call transcript, every data export, every relevant code path. "Complete" means you can say "I read all N tickets," not "I read a representative sample of tickets." Sampling hides exactly the kind of minority pattern (2 cases out of 20) that often turns out to be the real finding.

If the source list is large, this is a good candidate for Phase 6's parallelization — split by source type or by date range, not by skimming faster.

## Phase 3: Cross-reference on purpose

For each specific claim (a complaint, a metric, a quote), actively check it against the other sources instead of reporting it as a standalone fact:

- Does the quantitative data back up what the ticket says, at the same magnitude?
- Does the interview timeline match when the data actually moved?
- Do two sources describing "the same problem" actually describe the same mechanism, or two different ones that happen to look similar from a distance?

In the worked example, a weekly-aggregate usage chart looked like a single company-wide dip that was slowly recovering. Splitting it by individual user showed it was actually two very different populations averaged together: a handful of users driven to zero and staying there, and everyone else doing *better* than before. The aggregate hid the real shape entirely. This is the kind of thing cross-referencing on purpose catches and skimming doesn't.

Also check timing specifically: does a complaint's own stated timeline (e.g., "this has been happening for six days") line up with when the underlying cause could plausibly have started? A complaint whose own math puts its start before the suspected cause existed is a strong, checkable signal that something else is going on for that case.

## Phase 4: Show the work

Every number in your output traces to a source. In practice this means: file paths and line numbers for data claims, ticket or message IDs for qualitative claims, and showing the actual rows or quotes, not just a paraphrase, for anything load-bearing. This isn't about padding the output — it's what lets someone else (or you, later) catch a mistake in the underlying math instead of inheriting it silently.

## Phase 5: Write falsifiable hypotheses

See `hypothesis-format.md` for the template. The key discipline is ranking by resolvability, not by narrative appeal. The hypothesis that confirms the story you already suspect isn't automatically the one to chase first — the one you can actually test this week is.

## Phase 6: Parallelize open questions

When an investigation splits into genuinely independent angles — "does the data support theory A," "is this a client-side bug," "does the timing line up" — and subagents are available, send them out in parallel rather than working each one serially. Give each agent enough context to work without access to the rest of the conversation (they don't have it), a clear question, and instructions to report confidence and what would change their mind.

When they report back, do the synthesis work yourself: where did they agree, where did they disagree, and — importantly — did any of them turn up something that corrects the hypothesis you started with? In the worked example, one agent's analysis directly falsified a sub-claim of the leading theory (that the affected users shared a particular trait) by finding a counterexample in the same dataset. That correction was more valuable than any of the confirmations, and it only surfaced because the agents were genuinely independent rather than all converging on what they expected to find.

## Phase 7: Simulate before building

Before a fix or a feature spec is written, build a small model of the proposed mechanism and run it against real data: does it actually reproduce the pattern you're trying to explain? This catches mechanisms that sound right but don't actually produce the observed shape when you run the numbers.

Always attach a confidence score (0-100) to simulation output, and say explicitly what's approximated or assumed. If a key input doesn't exist in real data (a split you can't observe, a variable nobody logged), you can fill it with a synthetic/assumed value to see how sensitive the result is — but the output must say SYNTHETIC or equivalent, visibly, not buried in a caveat paragraph nobody reads. A synthetic-data confidence score should generally be lower than a real-data one, because synthetic data can't add evidence, only illustrate uncertainty.

## Phase 8: Communicate at the right altitude

The same finding needs different shapes for different readers:
- A full synthesis document, for you and anyone doing follow-up work: every source, every hypothesis, every number traced.
- A plain-language summary, for a fast read: what happened, why, what's next, no jargon.
- A short brief for a decision-maker: what you're confident about, what you're not, what you're doing about it, and one explicit decision you need from them if there is one.

Check first whether the decision-maker has stated what they actually want (a direct request, a prior ask, a document like a project brief) rather than assuming the investigation's own shape is what they're asking for. In the worked example, a director's actual request was a one-pager on a proposed experience, from the point of view of the people affected by it — not a replay of the investigation. Building the wrong-shaped document first wastes a cycle.

## Phase 9: Name the gap

End every output — synthesis doc, brief, prototype handoff — with what's still unverified and who owns closing it. This keeps a theory from being read as more settled than it is. It's also the single easiest thing to skip under time pressure, which is exactly why it's called out here as its own phase rather than folded into a caveats footnote.

## Phase 10: Prototype and iterate

Don't enter this phase by default just because phase 9 finished. Finishing the investigation with a ranked hypothesis list and a named gap is a complete, useful deliverable on its own. Move into building only when the user explicitly asked for something built, or the investigation was framed from the start (phase 0) as being in service of producing something. When it's time to build, ask which output fits rather than assuming: an interactive prototype, a one-pager, a PRD, or a slide deck with speaker notes are the usual menu, and they imply different amounts of work and different readers.

If a prototype is what's wanted: build something concrete for the leading hypothesis — an interactive page, a mock screen, a small tool — rather than only a written proposal. People react to things differently than they react to descriptions of things.

If real users aren't available for testing, simulated stakeholder feedback (role-playing plausible personas grounded in what you've actually learned about them) is a useful rehearsal for the real test. State clearly, every time this happens, that it's simulated and not a substitute for real user research — and don't let that framing soften over repeated iterations where it's easy to start treating the simulation's "feedback" as if it had become real.

Apply what the feedback (real or simulated) surfaces, and keep the most important caveats visible in the artifact itself — not just in the conversation where you built it — since the artifact is what gets shared onward.

## Worked example, condensed

A release changed how a system prioritized who to contact first, and user-reported problems split into two very different stories depending on the source. Tickets suggested a widespread problem; usage data suggested a narrow one. Working through the phases: gathering every ticket and interview (not a sample) surfaced a self-doubting tone in several reports that never appeared in interview transcripts — a real signal about who was affected and how they experienced it, invisible if only one source had been read. Cross-referencing ticket dates against the release date caught at least one complaint whose own timeline predated the cause it was blamed on. A hand-built simulation of the scoring mechanism, run against real usage data, reproduced the observed collapse almost exactly for the confirmed cases — and then, by being run against the *full* population rather than just the suspected cases, surfaced two more people on the same trajectory a few weeks behind, who hadn't been flagged yet. A parallel-agent investigation into "why these specific people" falsified the leading explanation for one of them and left the real distinguishing factor as an open, named gap rather than a forced answer. The final deliverables were three different documents (synthesis, plain-language summary, decision-maker brief) built only after confirming what the decision-maker had actually asked for, plus an interactive prototype that went through two rounds of simulated-user feedback before being handed off — each round clearly labeled as simulated.
