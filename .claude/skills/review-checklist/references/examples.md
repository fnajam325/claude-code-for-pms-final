# Worked examples

One pass and one fail per check, plus the edge cases that are easy to misjudge.

## 1. Names an owner

**Pass:** "Helen Achebe owns this and signs off on scope changes."
**Fail:** "Product will own the rollout plan." — a function, not a person. Nobody can say yes or no on its behalf.

**Edge case:** "The Dispatch team owns this; Marcus makes the final call on anything affecting routing." — pass. A team is named, but the brief also says who on that team actually decides, which is the part that matters.

## 2. Says how we'll know it worked

**Pass:** "We'll know this worked if time-to-accept drops below 45 seconds within four weeks of launch."
**Fail:** "This should make the console feel faster and more responsive." — no number, no way to be wrong.

**Edge case:** "Success is zero complaints about this in the first month." — pass, even though it's not a growth metric. It's falsifiable: either there are complaints or there aren't.

**Edge case:** "Increase acceptance rate." — fail, even though it names a real metric. No target and no timeframe means it can't actually be checked against.

## 3. Keeps one scope from start to finish

**Pass:** The brief opens with "This covers the responder-facing offer screen only, not the handler console," and every section that follows stays on the responder screen.

**Fail:** The brief opens scoped to "the offer screen," but a middle section quietly proposes changes to the handler's coverage view too, with no acknowledgment that this is outside the stated scope.

**Edge case:** A brief mentions a related handler-side change only to say explicitly "out of scope for this brief, tracked separately in [ticket]." That's not scope drift — it's a correctly-bounded brief naming an adjacent problem and declining to solve it here. Don't fail a brief for mentioning something it's explicitly not doing.

## 4. Explains the problem before the fix

**Pass:** Section 1 describes who's affected and what it costs them; section 2 proposes the fix in response to that description.

**Fail:** Section 1 opens with "We will add a confidence score to the availability view," and the problem it solves only shows up as a sentence two pages later, after the design is already specified.

**Edge case:** A one-paragraph brief states the problem and the fix in the same paragraph, problem first, fix second, with no separate headers. That's a pass — the check is about order and presence, not document structure or length.
