# What happened to Rook Dispatch around 4.2

*Rook Dispatch release 4.2 shipped on 12 Aug 2026. Evidence: four handler interviews (wiki, 2 to 5 Sept), 147 support tickets (database, 29 Jun to 7 Sep), 1,696 pings and 1,319 callouts (database, 29 Jun to 6 Sep), the routing code, and the company documents. Fictional teaching scenario.*

---

## 1. The story in plain words

Rook helps people called **responders** get jobs. When a job comes in, Rook sends it to one responder's phone. If they don't answer, Rook tries the next one.

**Before 4.2**, a responder had 90 seconds to say yes or no. Almost everyone answered in time. Each responder was asked about every job in their own part of the city.

**On 12 August, Rook made 4.2.** It did two big things:

1. It cut the time to answer from 90 seconds to 60 seconds.
2. It changed who gets asked first, so people who are closer count for more.

**Right away, many more offers went unanswered.** It went from about 2 out of every 100 offers to about 14 out of every 100. People did not say no more often. They just ran out of time.

**Rook also keeps a score for each responder.** Say yes and the score goes up a little. Say no, or run out of time, and the score goes down more. There is no other way to get points back. If your score is low, you get asked less. Then you have fewer chances to earn points.

**Four responders got stuck:** Farlight, The Undertow, Vesper, and Meteor Mite. They went from about 12 offers a week to about 4. When they were asked, they missed more than half of the offers. The other twelve responders got more offers.

**Their neighbours picked up the work.** The same nearby heroes had always been the backups for each area, and now they were first in line. The jobs still got done, but those neighbours got busier, and more of their own jobs went untaken.

**Their handlers noticed.** Handlers are the people who look after the responders. Some said, "The offer disappears before he can answer." Others said, "The phone is quiet and nobody can tell us why." Support tickets jumped from about 6 a week to about 25 to 30. None of the tickets about this have been closed. Many handlers did not know about the new 60-second limit. They asked, "Is that expected?"

**Jobs were hurt too.** Before, about 5 jobs in 100 ended with nobody saying yes. For three weeks after 4.2, it was about 13 in 100.

**What we know:** offers are being missed, not refused. The 60-second limit is real. Four responders lost most of their offers.

**What we don't know yet:** why those four miss so many. Either they answer a little slower, or their phones don't get the message. Engineering logs can tell us.

---

## 2. Table 1: the 4.2 problems and the evidence

Rows 1 to 7 are the original 4.2 problems. Rows 8 to 10 emerged after 4.2.

| # | 4.2 change | Problem statement | Interviews (4) | Tickets (147) | Pings | Verdict |
|---|---|---|---|---|---|---|
| 1 | Routing weights | I am a **responder across a wide geography**. I am trying to **get offered callouts close to me**, but I cannot because **a better-acceptance responder far away outranks me**, which makes me feel **unhappy and overlooked**. | No wide-geography responder was interviewed. Kip and Dot describe the opposite: a responder overlooked after 4.2. | None before 4.2. After: 32 "quiet" tickets from 4 responders. | Before: each responder was pinged on 100% of home-area callouts. After: twelve still are, four fell to 16-28%. Pings in their own area fell 83% to 61%. | **Not delivered for the intended group; recreated the problem for others** |
| 2 | Filter persistence | I am a **handler**. I am trying to **keep my console view**, but I cannot because **filters reset every session**, which makes me feel **annoyed at redoing setup**. | Ambrose (1 of 4): landed "within the hour", but resets silently after updates. | 2 before, 14 after (10 responders, 6 open). Only 4 are silent resets. 10 are side effects: wrong computer (2), shared sign-in (2), badge hard to see (2), can't clear (2), thank-yous (2). | n/a | **Delivered, with rough edges** |
| 3 | Fix: duplicate push | I am a **responder**. I am trying to **respond to one offer**, but I cannot because **I get a duplicate push on re-offer**, which makes me feel **confused**. | None | 3 before, 0 after. | n/a | **Looks fixed** (small numbers) |
| 4 | Fix: coverage report timezone | I am a **handler**. I am trying to **read the coverage export**, but I cannot because **the timezone is wrong**, which makes me feel **unable to trust it**. | None | 1 before, 0 after. (Two later tickets on availability-hours time zones are a different problem.) | n/a | **No complaints since** (weak) |
| 5 | Fix: capability tag order | I am a **handler**. I am trying to **read a responder's tags**, but I cannot because **they appear in the wrong order**, which makes me feel **unsure**. | Ambrose raised the tag legend, which is a different problem. | 1 before (ordering), 0 after. | n/a | **No complaints since** (weak) |
| 6 | Timeout 90s to 60s | I am a **handler**. I am trying to **get an incident assigned quickly**, but I cannot because **unanswered offers hold 90s**, which makes me feel **anxious**. *(Goal still unstated; my guess.)* | 3 of 4: offers vanish. Ambrose: a "slower response" used to still win. | None before, **13 after** from 9 responders (15 counting two that are also quiet), first on release day. 7 of 13 ask whether it's expected or how long the window is. All open. | Median wait after a miss 92s to 62s. Missed 2% to 13-21%. Declines flat. | **Cost clearly visible; goal not evidenced** |
| 7 | Availability Confidence | I am a **handler**. I am trying to **know whether an available responder will answer**, but I cannot because **only stated availability is shown**, which makes me feel **uncertain**. | Not raised. Handlers asked for a clearer live signal instead. | None | "Available" responders miss 59% (the four), so the gap it targeted is visible. | **Not shipped. Confirm with Helen.** |
| 8 | *Emerged* | I am a **responder who missed a few offers**. I am trying to **get offered callouts again**, but I cannot because **each miss costs 0.12, an accept earns back 0.08, and nothing else restores it**, which makes me feel **shut out**. | Kip (Mite), Dot (Vesper). | 32 quiet tickets (Farlight 11, The Undertow 11, Ashgrove 5, Halfmoon 5). 15 ask for an explanation. None closed. Handlers' ping counts match the pings table. | Four responders: offers 12 to 3-5 a week, missed 53-64%. | **Confirmed in code and data** |
| 9 | *Emerged* | I am a **handler**. I am trying to **get an incident covered**, but I cannot because **nobody takes the offer**, which makes me feel **exposed**. | Not raised. | Not raised. | Unfilled callouts 5% to about 13% for three weeks (about 29 extra), then 5.5% in the week of 31 Aug. Most of the rise is in the neighbours' areas (Southport, Riverside, Kingsbridge), not the four quiet ones (Table 2, row 34). | **Only visible in data** |
| 10 | *Emerged* | I am a **handler**. I am trying to **see that a callout is live and which responder it is for**, but I cannot because **alerts are indistinct**, which makes me feel **unsure**. | 3 of 4. | "Same alert sound" 1 before, 1 after. | n/a | **Real, not caused by 4.2** |

*Feelings are the analyst's wording, except "unhappy" in row 1. Rows 6 and 8 are the strongest, with all three sources agreeing. Rows 4 and 5 rest only on an absence of complaints. All 147 ticket bodies were read: the 32 quiet and 13 too-fast tickets were classified correctly, and no callout tickets were hiding in other themes.*

---

## 3. Table 2 (companion): findings that are not in Table 1

| # | Group | Finding | Source | Why it matters |
|---|---|---|---|---|
| 1 | Should be in the story | **Ashgrove and Halfmoon are mild cases.** Offers fell ~25-30% (their own handlers report 7-8 pings against a usual 10-11), still pinged on 100% of home callouts, miss 14-15% like everyone else. | Pings, tickets | The loudest filers aren't the worst hit. |
| 2 | Should be in the story | **Not all ticket growth is 4.2.** Supply and other console tickets also rose ~2.5x per week. Only the 45 quiet and too-fast tickets are clearly 4.2. | Tickets | Don't credit the whole 4x to 4.2. |
| 3 | Should be in the story | **Handlers don't know about the 60-second limit.** 7 of the 13 too-fast tickets ask "is that expected?" or how long the window is. Ticket 3043 asks for the timing to be confirmed and is still open. | Tickets | The change wasn't understood and reports get no answer. |
| 4 | Should be in the story | **Nothing has been closed.** Pre-4.2 tickets all closed. 83 of 107 since are open, including all 45 on silence and vanishing offers. | Tickets | Support has no answer yet. |
| 5 | Should be in the story | **Busy responders are strained.** The Gale +43% offers, Nightwell ~+25%. Kip: "Gale's exhausted." | Pings, interviews | A burnout and churn risk among the busiest. |
| 6 | Should be in the story | **No tickets at all** for Vesper, Meteor Mite, The Gale, Bulwark. | Tickets | The queue understates the problem. |
| 7 | Ruled out | **Geography as the cause of the lock-out.** Mite and Gale share Eastgate with opposite outcomes. The four are in four of the six busiest areas. Geography does decide who steps in: see row 33. | Pings | Distance alone doesn't explain who got locked out. |
| 8 | Ruled out | **Time of day.** The four miss 50-77% at every time of day. | Pings | Not a night or morning effect. |
| 9 | Ruled out | **Cascade position.** The four are first in line 71% of the time, like everyone else. | Pings | They aren't being pinged "late". |
| 10 | Ruled out | **Seasonal as the main cause.** Callouts logged fell ~14%, which can't explain misses rising tenfold on release day. | Pings, callouts | The "August is soft" read is small. |
| 11 | Smaller data point | **Declines are quick.** Median 22s (range 6-40s). | Pings | People who refuse decide fast. |
| 12 | Smaller data point | **More cascading.** Pings per callout rose from ~1.25 to 1.3-1.6. | Pings | More handoffs per incident. |
| 13 | Smaller data point | **Day one.** 7 of 9 pings to the four were missed on 13 Aug. | Pings | Onset is immediate, not gradual. |
| 14 | Smaller data point | **Repeat filers.** Farlight's and The Undertow's handlers filed 19 and 21 tickets, with escalating quotes. | Tickets | Strong, sustained signal from two handlers. |
| 15 | Smaller data point | **Pre-4.2 warning signs.** An accidental decline that cost a job (3033), a miss from lost signal (3014), push unreliable on older phones (3034). | Tickets | Delivery and accidental penalties already worried handlers. |
| 16 | Smaller data point | **Acceptance rate misleads.** 0.77 to 0.54 to 0.73, but the recovery is partly because the four's offers left the average. | Pings | The headline metric hides the damage. |
| 17 | Smaller data point | **Unfilled callouts recovered** to 5.5% in the week of 31 Aug. Unexplained. | Pings | Need to know whether it's durable. |
| 18 | Code and documents | **60% break-even.** A responder needs to accept about 60% of offers to hold their score. | Code | Below that, the score drifts to the floor. |
| 19 | Code and documents | **Proximity dominates.** The whole acceptance range is now worth ~19 minutes of travel, down from ~40. | Code | Being slightly far matters more than history. The weights did not make location matter less. The home heroes' scores hit the floor (row 33). |
| 20 | Code and documents | **Glossary vs. code.** The glossary says scores "recover", but the code only restores points by accepting. | Glossary, code | Written material misleads. |
| 21 | Code and documents | **Marcus's 14 Aug question** (does the change apply to responders who've been declining?) is still unanswered. | Slack | Intent is undocumented. |
| 22 | Code and documents | **Supply reads Dispatch's availability record.** The shifted callout load may affect maintenance scheduling. Unverified. | One-pagers | A cross-product effect nobody has checked. |
| 23 | Data we lack | **Time-to-accept and tap latency** per responder. | none | Would separate "slow" from "undelivered". |
| 24 | Data we lack | **Push delivery logs.** | none | Would show whether pings reach the phone. |
| 25 | Data we lack | **Actual score history.** | none | Would confirm the penalty loop directly. |
| 26 | Data we lack | **Any responder's own voice.** All four interviews are handlers. | none | We know what handlers see, not what responders feel. |
| 27 | Data we lack | **Revenue or churn.** Pricing is per active responder. | none | Business impact is unsized. |
| 28 | Added after reading all 147 tickets | **Handlers' ping counts match the database exactly.** Farlight: 23 Aug then 28 Aug. The Undertow: 21 Aug, 27 Aug, 5 Sept. Since 18 Aug, 0 of 8 pings to these two were taken. | Tickets, pings | Handlers are reliable witnesses. |
| 29 | Added after reading all 147 tickets | **Half the quiet tickets ask for an explanation** (15 of 32): "Could someone check yours?", "I would rather know than guess". | Tickets | Support has no answer to give. |
| 30 | Added after reading all 147 tickets | **Filter persistence needs polish.** Only 4 of 14 post-4.2 filter tickets are silent resets. 10 are side effects of the feature. | Tickets | Delivered, but with follow-on problems. |
| 31 | Added after reading all 147 tickets | **Two tickets booked maintenance on the busiest day of the year** (3054 on 15 Aug, 3109 on 29 Aug). None before 4.2. | Tickets | A weak hint about Supply scheduling. Unverified. |
| 32 | Added after reading all 147 tickets | **Repeated wording.** 25 of the 107 post-4.2 tickets repeat earlier text word for word. None did before. | Tickets | Treat ticket counts with care: 97 distinct texts vs. 40. |
| 33 | Added after the map | **Neighbourhoods are fixed.** Every hero was pinged for the same 1 to 3 other areas before and after 4.2, and no hero was pinged for a new area. The same neighbours back up each area (Uptown: Falkirk, Cindermark, Bulwark; Old Town: Vantage, Nightwell, Longcast; Harborside: Stormwrack, Ironvale, Drift). | Pings | Location still decides who backs up whom. What changed is that three home heroes stopped being first in line. |
| 34 | Added after the map | **Nobody took it rose in the neighbours, not in the quiet areas.** The four quiet areas' own untaken jobs went from 17 to 11 (about 2.7 to 3.0 a week). Southport went 3 to 9, Riverside 2 to 6, Kingsbridge 4 to 6: the home areas of heroes who picked up the quiet areas' work. Overall 5% to 11%. | Pings, callouts | The spill-over lands on the neighbours. |
| 35 | Added after the map | **The "too fast" complaints come from the heroes who picked up the quiet areas' jobs.** 8 of the 9 responders in the 13 too-fast tickets (Drift, Vantage, Falkirk, Ironvale, Nightwell, Stormwrack, Cindermark, Longcast) are heroes who took jobs outside their home base. Halfmoon is the exception. Bulwark, also one of them, raised it in his interview. Their miss rates are not higher (10-18%, like everyone else). They just have more offers. | Tickets, interviews, pings | The two symptoms are linked. The neighbours are carrying two areas and feel the 60-second window most. |

---

## 4. Two responders side by side

Two responders from the database, one who went quiet and one who didn't. Both are in the 16-responder roster. 4.2 shipped on Wed 12 Aug.

### Farlight (went quiet): Uptown, handler Linda Pruitt

| Week starting | Jobs in her home area (any responder) | Pinged | of which for home-area jobs | of which for jobs elsewhere | Taken | Turned down | Missed |
|---|---|---|---|---|---|---|---|
| 29 Jun | 10 | 12 | 10 | 2 | 9 | 3 | 0 |
| 6 Jul | 10 | 12 | 10 | 2 | 9 | 3 | 0 |
| 13 Jul | 8 | 11 | 8 | 3 | 8 | 2 | 1 |
| 20 Jul | 10 | 12 | 10 | 2 | 9 | 2 | 1 |
| 27 Jul | 11 | 13 | 11 | 2 | 10 | 3 | 0 |
| 3 Aug | 8 | 12 | 8 | 4 | 8 | 3 | 1 |
| **10 Aug** (4.2 ships) | 6 | 10 | 6 | 4 | 4 | 2 | 4 |
| 17 Aug | 7 | 3 | 2 | 1 | 0 | 1 | 2 |
| 24 Aug | 10 | 1 | 0 | 1 | 0 | 0 | 1 |
| 31 Aug | 10 | **0** | 0 | 0 | 0 | 0 | 0 |

*How to read this table: "Jobs in her home area" counts every job that happened in her area, whoever was pinged. "Pinged" counts every time her phone was asked, including jobs elsewhere, so it can be higher than the jobs in her area.*

**In plain English**

- **Six steady weeks (29 Jun to 9 Aug).** About 12 offers a week, about 9 taken (three in four). Only 3 misses in six weeks. She was asked about nearly every job in her area.
- **The week 4.2 shipped.** The first two days were normal. From Wednesday evening to Friday afternoon she missed four offers in a row, as many as in the previous six weeks combined. She took two others.
- **Week of 17 Aug.** Only 3 pings, and only 2 of the 7 jobs in her own area. She took none. On 17 Aug her handler wrote that her phone "has not gone off in three days".
- **Week of 24 Aug.** One offer, on Friday evening, gone before she could answer. It was her first in five days, and it was for a job elsewhere: none of her own area's 10 jobs reached her. Her handler wrote that she had started "asking me every day whether something is broken".
- **Week of 31 Aug.** Nothing at all, though 10 jobs happened in her area. Her own words, passed on by her handler: "nothing again this week. starting to wonder if im still even in the system."

**After 4.2:** pinged 11 times, took 2, missed 7, turned down 2. Her last take was Fri 14 Aug. She is not refusing: she turned down only 2 offers. Estimated score (replay of the code's rules, so an estimate): about 0.84 before 4.2, zero on 23 Aug.

### Captain Vantage (not quiet): Hillcrest, handler Mr. Ambrose

| Week starting | Jobs in his home area (any responder) | Pinged | of which for home-area jobs | of which for jobs elsewhere | Taken | Turned down | Missed |
|---|---|---|---|---|---|---|---|
| 29 Jun | 11 | 12 | 11 | 1 | 10 | 2 | 0 |
| 6 Jul | 10 | 13 | 10 | 3 | 10 | 2 | 1 |
| 13 Jul | 8 | 12 | 8 | 4 | 8 | 4 | 0 |
| 20 Jul | 8 | 11 | 8 | 3 | 7 | 3 | 1 |
| 27 Jul | 9 | 12 | 9 | 3 | 9 | 3 | 0 |
| 3 Aug | 10 | 12 | 10 | 2 | 9 | 3 | 0 |
| **10 Aug** (4.2 ships) | 8 | 13 | 8 | 5 | 8 | 4 | 1 |
| 17 Aug | 9 | 15 | 9 | 6 | 11 | 2 | 2 |
| 24 Aug | 9 | 17 | 9 | 8 | 13 | 3 | 1 |
| 31 Aug | 7 | 18 | 7 | 11 | 13 | 3 | 2 |

*How to read this table: "Jobs in his home area" counts every job that happened in his area, whoever was pinged. "Pinged" counts every time his phone was asked, including jobs elsewhere, so it can be higher than the jobs in his area.*

**In plain English**

- **Six steady weeks (29 Jun to 9 Aug).** 11 to 13 offers a week, about three in four taken. Only 2 misses in six weeks.
- **The week 4.2 shipped.** On Wed 12 Aug at 7:03pm he missed an offer. That is the callout Ambrose wrote about the next day ("coat and one boot on"). It was his only miss that week. He was pinged again the next day and carried on.
- **After 4.2 (17 Aug on).** His offers rose from about 12 a week to 15, 17, then 18. He took 11 to 13 a week against 9 or 10 before, and was still taking about 71% of what he was offered. He was catching work the quiet responders weren't getting.
- **Where the extra offers came from.** All of them were for jobs outside Hillcrest: 1 to 4 a week before, then 5, 6, 8, and 11. He was still pinged on every Hillcrest job.
- **The cost.** He misses more: 10% of offers against 3% before, so 1 or 2 a week. More offers also means more strain.

**After 4.2:** pinged 59 times (76 before, over a longer period), taken 71% against 74%, missed 10% against 3%. Estimated score (replay, so an estimate): about 0.96 before and about 0.92 at the end, essentially unchanged.

### Side by side

| | Farlight | Captain Vantage |
|---|---|---|
| Offers after 4.2 | fell from 12 a week to 0 | rose from 12 a week to 18 |
| Share of offers missed | 64% | 10% |
| Take rate | collapsed | about the same (74% to 71%) |
| Taken since 14 Aug | none | 11, 13, 13 a week |

**What this tells us**

- **The 60-second window hurts everyone a little.** Even someone still doing well misses more.
- **Only some people fall off a cliff.** Vantage's score stays high because he keeps getting offers, so each miss is made up by his accepts. Farlight started missing, her score fell, and the offers that would have let her recover stopped coming.
- **The risk for busy responders is strain, not a lock-out.** More work lands on the same few people (Kip: "Gale's exhausted").

---

## 5. Open questions and next steps

- **Engineering (Marcus, Wen):** tap-latency and push-delivery logs for the four, the real score history, and whether the weights were meant to apply to responders who had been declining.
- **Helen:** why the timeout is 60 seconds, what success was meant to look like, and whether Availability Confidence slipped.
- **Ravi:** confirm the weekly numbers and why unfilled callouts recovered in the week of 31 Aug.
- **Support (Nadia):** a reply to the open tickets, especially 3043.

### Already answered or narrowed

- **Weekly numbers:** the repo's CSV and the database tie out exactly for all ten weeks.
- **Real score history:** not available, but replaying the pings through the code's rules gives an estimate. The four were at 0.84-1.00 before 4.2 and hit the floor on 21, 23, 26, and 29 Aug. The other twelve dipped and recovered. Estimate only.
- **Unfilled callouts in the week of 31 Aug:** 7, inside the pre-4.2 range of 4-12. The twelve answered more of their pings (missed 16% down to 11%). The four contributed 3 pings. One week of small numbers.
- **Why 60 seconds, and what success meant:** not written down. The wiki roadmap rows for 4.2 say only what to change.
- **Availability Confidence:** absent from release notes, changelog, code, and the wiki 4.2 page, but its roadmap row still says "Committed". Needs Helen.
- **Marcus's reply on 26 Aug** ("That'll be the August dip... Should settle once September starts") is in the wiki and not in the repo's Slack export. It conflicts with the data.

### Confidence

About 75 out of 95 overall. The counts and rates are high (about 90). The causal story is lower: the penalty loop about 60, and why the four miss so much about 35, until the tap-latency and delivery logs arrive.

*Method notes: tickets were first grouped by subject-line keywords, then all 147 bodies were read and the callout themes confirmed. "Missed" means no answer within the window and includes undelivered pings. The week of 10 Aug mixes before and after 4.2. Areas are coarse.*
