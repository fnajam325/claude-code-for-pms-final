# Hypothesis format

Write every hypothesis as one block with these five parts. The point of the format is that a reader can see exactly what would prove the hypothesis wrong without asking you — if they can't, it isn't falsifiable yet.

```
**[Short name]**
If [the proposed cause], then [the observable effect], because [the mechanism connecting them].
- Confirms if: [the specific data pattern that would support it]
- Fails if: [the specific data pattern that would rule it out]
```

## Ranking hypotheses

Rank by how resolvable each one is with data you can plausibly get, not by how interesting or central it sounds. A table like this makes the ranking visible:

| # | Hypothesis | Confirms if | Fails if | Data needed | Resolvable how soon |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | Already have it | Now |
| 2 | ... | ... | ... | One data pull | This week |
| 3 | ... | ... | ... | Needs weeks to observe | Later |

A hypothesis that would take a month to test isn't wrong to include, but it shouldn't sit above one you can resolve today with data already in hand.

## Common failure modes to avoid

- **Unfalsifiable hypotheses.** "Something about the release caused this" has no confirms-if or fails-if. Push until you can name the specific observable pattern on each side.
- **Confirmation-shaped testing.** Don't just check whether the data could be consistent with the hypothesis — check whether it's also consistent with the alternative. If it is, the test doesn't discriminate between them and isn't done yet.
- **Treating a simulation as a test.** A simulation built from the proposed mechanism will usually "confirm" the mechanism, because it's built to. That's a demonstration of plausibility, not a test. Real confirmation comes from data the simulation didn't generate.
- **Silently dropping a hypothesis that failed.** Record it anyway, with what killed it. A failed hypothesis is useful context for whoever reads this later and wonders why an obvious explanation wasn't the answer.
