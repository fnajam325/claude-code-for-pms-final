# Module 5 session log

## 22 Oct 2026: the brief for Helen, a clickable prototype, and two rounds of simulated user testing

### Goal
Turn the 4.2 findings into a one-page brief for Helen and a clickable prototype of the fixes that she could click through, then test the prototype with simulated handlers and responders and iterate.

### Findings
| Finding | Evidence and source | Confidence | Status |
|---|---|---|---|
| Meteor Mite's last offer before the gap was 22 Aug at 20:53 (not taken). Later offers: 27 Aug 20:03 declined, 29 Aug missed, 5 Sept missed. Mite took none after 19 Aug. | `pings` table, responder = Meteor Mite | Observed | Confirmed |
| In the 7 days to 25 Aug 21:00 Meteor Mite had 3 offers against a usual 11.2 a week (down 73%). The Gale had 15 against a usual 13.0 (up 15%). "Usual" = the six weeks 29 Jun to 9 Aug. | `pings` table | Observed | Confirmed |
| Gaps of 3+ days between consecutive offers, six weeks before 4.2: The Drift 3, The Gale 2, Ironvale 1, Farlight 0, Meteor Mite 0, Halfmoon 0, Stormwrack 0. After 12 Aug: Farlight 2, Meteor Mite 2. So a flat 3-day rule fires on healthy low-volume responders. About six of the brief's seven "other twelve" cards would come from these three. | `pings` table (gap measured between consecutive offers) | Observed for the gaps; estimated for the "six of seven" (I did not recompute all twelve) | Open: needs a per-responder rule tested by Ravi |
| Farlight's last offer before the long gap was 14 Aug (21:22), so the card fires 17 Aug, the same day as Linda's first ticket (3060), not before. Her weekly count of 3 vs a usual 12 is exactly a quarter, so the weekly rule would not fire. Every Farlight offer from 19 to 28 Aug was missed or declined. | `pings` table, `support_tickets` | Observed | Confirmed |
| "Close the case when an offer arrives" is wrong: it would close cases on offers nobody answered (Farlight 19-28 Aug; Meteor Mite 27 Aug, which was declined). | `pings` table | Observed | Fixed in prototype v3; the brief still has the old rule |
| In v2, white text on the green pill was 3.5:1 (light theme) and 1.7:1 (dark theme); the orange focus ring was invisible on the orange alert strip; the focused button was disabled on nearly every action, losing keyboard focus; changes were not announced. | Screen-reader audit of the HTML, plus my own contrast calculation from the hex values | Observed | Fixed in v3; not tested in a real screen reader |
| Simulated round 1 (8 testers): all 4 handlers read "Dismiss" as "handled"; 6 of 8 said "I'm stepping back" felt like quitting; 5 of 8 said "we're looking into why" is empty. | Role-played testers; handlers built from the real interviews | Guess (simulated) | Acted on in v2 |
| Simulated round 2 (8 role-played testers + 1 audit): "we're looking into why" 8 of 8; the v2 check-in blamed the phone 6 of 8; Pause caused trouble 7 of 8; nowhere for "something looks wrong" to go 5 of 8; delivery visibility wanted 5 of 8; closing on one offer too early 5 of 8. | Role-played testers built from each person's real tickets and weekly offer counts | Guess (simulated) | Acted on in v3, except the items listed under Open questions |

### Corrections
| What we believed | What we found | Why |
|---|---|---|
| Prototype v1 used "his", "himself" and "he" for Meteor Mite. | Sources give no pronoun for Meteor Mite. | Removed in v1.1; use "they" or the name. |
| The example happens at 9:00 on 25 Aug. | Meteor Mite's last offer was 22 Aug at 20:53, so the 3-day mark falls on the evening of 25 Aug. | Moved to 21:00 in v3. |
| The Gale's card showed "3 offers today, usually 13 a week". | At 9:00 that was not yet true, and it read as calm while The Gale was carrying more. | Replaced by a last-7-days line on every card in v3. |
| v2's check-in ("Is anything looking wrong on your phone?") fixed the blame in v1. | It moved the blame from availability to the phone (6 of 8 in round 2). | Rewritten in v3. |
| The case ends when an offer arrives. | Offers can go unanswered. | The watch ends only when the responder takes an offer (v3). |
| The first Helen panel was judging the brief alone. | It had also read other files, including prototypes. | I reran it with the brief text pasted and no tools, after the student's challenge. |
| v4 of the brief mentioned "last year's data". | The real window is 29 Jun to 6 Sept. | Corrected before the v4 save. |
| Three round-2 responders said "Kip has your answer" was the wrong name. | My round-2 script said "Kip" for every handler. It was my script, not the prototype. | Ignored. |

### Decisions
- Prototype scope (student's answers): promises 1 and 2 only; a scripted walkthrough; one page showing two devices; extra moments for the reply and the hidden card; a comic-book look; a push plus a banner; wording as drafted; a file plus a private artifact.
- Not built: promise 3, options A/B/C for the four, the stop rules.
- v2 and v3 changes: proposed by me from the test findings, approved by the student ("yep") and built.
- Turned down in v3: Pause as a reply to a "why no offers?" message; closing the watch on any offer; "case" and "still quiet" wording.
- Brief recommendation (option C now, B once Wen signs off): written in the brief. The student has not yet confirmed it is their own view.
- Sharing: the artifact was private when published; it was later set to "Anyone with the link" from the Share menu, not by me.

### Deliverables
- `05-super-speed/helen-brief-v4.md` and `helen-brief-v4-reference.md`: the brief and its detail page (saved to GitHub earlier this session). Still carry the v1 wording of the check-in and the close rule.
- `05-super-speed/quiet-responder-prototype.html`: prototype v3. Artifact: https://claude.ai/artifact/PPRL62aqpZuG7UXrTus91w (anyone with the link).
- `05-super-speed/quiet-responder-prototype-changelog.md`: v1 to v3, each change with its reason, plus a "not changed, and why" table.
- `05-super-speed/archive.md`: older CLAUDE.md sections moved out on 22 Oct.
- Earlier in this session (Module 2 work): see `02-super-hearing/`.

### How to reproduce
Offers for a responder around a date:
`select sent_at, outcome from rook.pings where responder='Meteor Mite' and sent_at >= '2026-08-12' order by sent_at`
Last 7 days vs usual:
`select responder, count(*) filter (where sent_at >= '2026-08-18 21:00' and sent_at < '2026-08-25 21:00') last7, count(*) filter (where sent_at >= '2026-06-29' and sent_at < '2026-08-10')/6.0 usual from rook.pings where responder in ('Meteor Mite','The Gale') group by 1`
Gaps of 3+ days:
`with g as (select responder, sent_at, lead(sent_at) over (partition by responder order by sent_at) nxt from rook.pings) select responder, count(*) filter (where nxt-sent_at >= interval '3 days' and sent_at < '2026-08-12') before, count(*) filter (where nxt-sent_at >= interval '3 days' and sent_at >= '2026-08-12') after from g where nxt is not null group by 1`
Contrast: WCAG ratio (L1+0.05)/(L2+0.05) from the hex values; white on #0f9d58 is about 3.5:1.
Simulated testing: persona sheets from `support_tickets`, the four wiki interviews and `pings`; each tester gets a text script of the screens, no tools; count how many of 8 raise each point.

### Open questions
- Are Meteor Mite's missed offers slowness or offers that never reach the phone? (Wen; delivery logs from Ravi)
- Do scores survive a restart, and was "a miss counts like a refusal" intended? (Wen)
- Who is "we" in "we're looking into why", and by when? Or drop the line. (Helen)
- Can the card's check-in truthfully say "your availability and tags look right from here"? (Wen, Marcus; Security for the wording)
- A rule that scales to each responder's own gaps, tested on the pre-4.2 data. (Ravi)
- A dated "on leave" status: separate item. (Helen, Marcus, Sofia)
- Where do handlers who do not live in the console get alerted? (Marcus, Sofia)
- Is "C now, B once Wen signs off" my own recommendation? (the student)
- Do real handlers and responders react the way the simulated ones did? (needs real users)

### Prompts and moves that worked
- "Assume no prototypes exist yet and have them solely judging on the brief alone": isolated the panel from outside material and changed the result.
- "Ask me clarifying questions until you are 95% confident": settled the prototype scope in a few multiple-choice answers.
- "Run another round of testing with a different set of users": showed v2's fix had only moved the blame.
- Build each tester from that person's real tickets and offer counts, then count "n of 8" per finding.
- Check the testers' claims against the database before acting (it confirmed Linda's timing point and The Drift's false-alarm complaint).

### Start here next time
1. `05-super-speed/quiet-responder-prototype-changelog.md`: the "not changed, and why" table.
2. `05-super-speed/helen-brief-v4.md`: update it to the v3 wording and the close rule before sending to Helen.
3. This log's Open questions: send the first two to Wen and Helen.
