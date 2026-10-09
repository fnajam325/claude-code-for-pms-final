---
name: review-checklist
description: Use this skill whenever the user points at a brief, PRD, one-pager, proposal, or spec and asks to review it, check it, or sanity-check it before it goes out. Trigger on phrases like "review this brief," "check this before I send it," "does this brief hold up," "run the checklist on this," or when the user names a specific document and asks whether it's ready. Checks four things: the brief names an owner, states how success will be measured, keeps one consistent scope from start to finish, and explains the problem before the fix. Make sure to use this whenever a brief-like document is the subject, even if the user just asks "is this good?" or "anything missing?" without naming the checklist explicitly.
---

# Review checklist

Four checks, run against one document. Each one exists because a brief that fails it tends to fail in a specific, predictable way later — not because it's a rule for its own sake.

## The four checks

1. **Names an owner.** A specific person, not a team or a role left unassigned ("Product will decide," "TBD"). A brief with no owner is a brief nobody is actually accountable for — decisions drift, and when something goes wrong there's no one to ask. A named team is acceptable only if the brief also says who on that team makes the call.

2. **Says how we'll know it worked.** An explicit, checkable statement of success — a metric with a target, a specific observable outcome, or a decision point ("we'll know by X happening"). "Improve the experience" or "make this better" doesn't count; neither does a metric with no target ("increase conversion," with no number or timeframe). Without this, the brief can't fail even if it does nothing, because nobody defined what failing would look like.

3. **Keeps one scope from start to finish.** What the brief says it covers at the start matches what it actually covers by the end. Look for the opening scope statement (or the absence of one) and compare it against what shows up later — a new surface, a new user type, or a new problem introduced partway through that was never in the stated scope. This is the one check that requires reading the whole document, not just scanning for a sentence; scope drift usually shows up as an aside buried in the middle, not an edit to the opening paragraph.

4. **Explains the problem before the fix.** The document establishes why something needs to change — what's broken, for whom, and what it costs — before it proposes what to do about it. A brief that opens with the solution and backfills the justification after tends to mean the solution came first and the problem was found to justify it, which is worth surfacing even when the solution turns out to be right.

See `references/examples.md` for a worked pass/fail example of each check, including the edge cases that are easy to misjudge (an implied owner, a vague-sounding metric that's actually fine, scope drift that looks like helpful context).

## How to run it

1. Read the whole document before judging anything — all four checks, especially scope and ordering, require seeing the full thing, not just the opening section.
2. Judge each of the four checks independently. A brief can pass three and fail one; don't let a strong brief overall soften a real miss on one check.
3. For every check, cite the specific text that makes it pass or fail — a quote or a close paraphrase with its location in the document (a heading, a paragraph position). "No success metric" is a claim; show where you looked and what you found instead, the same way you'd want backed up data in Dashboard answer rather than a flat assertion.
4. If a check fails, say what's missing in one sentence and, if it's obvious, what adding would look like — not a rewrite of the brief, just enough to point at the gap.

## Output format

Report each check as pass or fail with its evidence, then one line of overall judgment. Use this shape:

```
**Owner:** Pass/Fail — [quote or citation, or what's missing]
**Success criteria:** Pass/Fail — [quote or citation, or what's missing]
**Consistent scope:** Pass/Fail — [quote or citation, or what's missing]
**Problem before fix:** Pass/Fail — [quote or citation, or what's missing]

[One sentence: how many passed, and whether the failures are small fixes or a sign the brief needs a rewrite.]
```

Don't pad a passing check with praise, and don't soften a failing one — the point of running this is to get a fast, honest read, not a cheerleading pass.
