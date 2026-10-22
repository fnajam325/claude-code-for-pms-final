# Reference for the Helen brief (v4)

Detail behind `helen-brief-v4.md`. Numbers come from the Rook database (pings and callouts tables), before = 29 Jun to 11 Aug, after = 12 Aug to 6 Sept. Dated 22 Oct 2026.

## Words used
- **Missed:** no answer in time. **Declined:** the responder tapped no. Both cost 0.12 today.
- **Jobs nobody took:** every responder asked either missed or declined.
- **Area:** the part of the city where a responder usually works, from our database. We do not hold exact locations.

## How we will know it worked (full table)

| Measure | Goal | Owner |
|---|---|---|
| Offers a week for each of the four | At least 8 (70% of their 11 to 14 before 4.2), with at least 9 in 10 answered in time, within 4 weeks of release. For comparison, the four answered 97 in 100 before 4.2, under the 90-second timer (all responders: 98 in 100). The 9 in 10 target allows for the shorter 60-second timer. | Ravi reports, Faran owns |
| Responders with no offers 7 days after a card was shown | Zero. A dismissed card does not count as handled. | Faran |
| Jobs nobody took | No more than 2 points above the level on the day promise 3 ships (5% before 4.2, 11% since) | Ravi |
| The other twelve say yes | No more than 5 points below the level on the day promise 3 ships | Ravi |
| Time to accept | No more than 10% slower than on the day promise 3 ships. Ravi pulls the baseline first. | Ravi |

The stop lines are proposals. They are set as changes from the level on launch day so that they measure promise 3, not the damage 4.2 already did.

## The card rule, from the data
It shows after 3 days with no offers, or when a responder has under a quarter of their usual offers in 7 days. "Usual" is the average over the first six weeks (29 Jun to 9 Aug). It shows once a week at most per responder. Dismissing a card does not close the case: the responder stays on the list until they get an offer.
- **The four:** it would have fired 10 times in total: Farlight 3 (first on 17 Aug), Vesper 3 (first on 22 Aug), The Undertow 2 (first on 24 Aug), Meteor Mite 2 (first on 25 Aug).
- **The other twelve:** 7 times in total across 9 weeks, under one a week across all twelve of them, not one each.

## Replay of the four's real offers
New rules: a missed offer costs 0.02 and only after 3 in a row, offers outside the responder's own area cost nothing, a refusal still costs 0.12, the lowest allowed score is 0.2, and the score rises toward neutral (0.5) only when it is below it.

| Responder | Today's rules: lowest / on 6 Sept | New rules (all three speeds of rise, 0.01, 0.02, 0.03 a day) |
|---|---|---|
| Meteor Mite | 0.00 / 0.00 | 0.46 / 0.96 |
| Farlight | 0.00 / 0.00 | 0.50 / 0.88 |
| The Undertow | 0.00 / 0.00 | 0.50 / 0.98 |
| Vesper | 0.00 / 0.00 | 0.50 / 0.88 |

**Limits.** The replay starts each responder at neutral on 29 Jun with the new rules in place all along. The speed of the daily rise made no difference, so the gentler penalties did all the work. It does not show how a responder already at zero would climb back, and it cannot show the offers they would have been sent. From the 0.2 lowest score, a rise of 0.02 a day reaches neutral in 15 days, and 0.01 a day in 30. The numbers 0.02, 0.02 and 0.2 are guesses: small enough that a few misses do not sink a score, and high enough to keep a responder in the pack.

## What Supply would see
Supply uses a record of when each responder is likely to be called out, and books gear repairs into quiet windows. Giving quiet responders offers again changes their windows. Dispatch's code says to tell Supply before shipping a change to that record.

## The 45 open tickets (as of 7 Sept)
32 about quiet responders (Farlight 11, The Undertow 11, Ashgrove 5, Halfmoon 5) and 13 about offers that vanished. Meteor Mite and Vesper have none: their handlers did not file tickets.

## Watch list
Halfmoon and The Drift say yes to 6.4 in 10, the lowest of the other twelve. Ashgrove and Halfmoon had offers fall by about 25% to 30%. Promise 1 covers every responder, so they are included.

## Sources
The Rook database, handler interviews, and the routing code. Availability Confidence (committed for 4.2, never shipped) is a separate conversation with Helen and is not part of this brief.
