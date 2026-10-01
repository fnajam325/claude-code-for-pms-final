# Console + support feedback synthesis

Interactive triage board (interviews): https://claude.ai/artifact/Dt7XNPmeVefB2u6DhAJRvg

Two sources, read together:
- **Interviews** — Sofia Marino's console redesign research, 2–5 Sept 2026, in `00-rook/feedback/interviews/` — Ambrose (handler, Captain Vantage), Dorothy "Aunt Dot" Pell (handler, Vesper), Halloran (handler, Sgt. Bulwark), Kip (handler, Meteor Mite & The Gale).
- **Support tickets** — 25 tickets, 13 Aug – 5 Sept 2026, in `00-rook/feedback/tickets/`.

## Plain-language summary

We talked to 4 people who watch the hero screens for a living. We read 25 notes from people asking for help. We looked at a big spreadsheet of numbers. Then we checked if all three agreed with each other.

**The big problem:** After a software update on August 12th, something broke. 4 heroes — Farlight, Meteor Mite, The Undertow, and Vesper — used to get about 12 jobs a week. Now they get 0 or 1. Every single week it got worse, never better. It's like the computer forgot they exist.

**Why it's happening:** The update changed the rules for who gets picked for a job. It now cares much more about "who is closest" and much less about "who says yes a lot." These 4 heroes used to say yes almost every time — that's actually why they used to get picked, even though they live far away. Now that doesn't count as much, so they stopped getting picked at all. Once a hero stops getting picked, there's no way built into the system to fix itself. It just stays broken.

**The tricky part — a second, different problem:** 9 other heroes also complained about being ignored. But when we checked their real numbers, most of them are actually getting the same or more jobs than before. So something else is going on with them — maybe they're just worried after hearing others complain, or maybe there's a totally different bug, like notifications not popping up on their phones. We don't know yet. That's a new mystery to solve.

**A trick with the numbers:** If you just look at "how often do heroes say yes," it looks like things are getting better. But that's a little bit of a magic trick — the number only looks better because the 4 broken heroes stopped getting offered jobs at all, so they stopped dragging the average down. The real amount of work getting done each week is still lower than before. It didn't actually get better. It just looks that way.

**One more clue — timing:** People started complaining the very next day after the update. But the real numbers didn't actually break for about 5 more days. So some complaints came in super early — even one that started before the update even happened, which means the update can't be the reason for that one at all.

**Bottom line:** There's one real, provable problem (4 heroes locked out, and it's the update's fault), one honest metric that's lying a little bit, and one big unsolved mystery (9 more people who feel ignored for reasons we haven't found yet).

## The one-sentence read

Based on the interviews, the trouble with 4.2 is that it quietly locked a handful of responders out of the rotation almost entirely, while making everyone else's offers vanish faster than they can react — and it's the same routing change causing both.

A teammate independently framed the same evidence differently: *"the trouble with 4.2 is nobody asked about callouts. Three of the four handlers brought them up anyway."* That's the credibility argument (unprompted, off-topic, and still volunteered by 3 of 4); mine is the mechanism argument (what's actually broken). Worth keeping both — they cover different pieces: the "3 of 4" framing is precise for the vanishing-callout complaint specifically (Ambrose, Dot, Halloran); it doesn't cover Kip's complaint, which is a different symptom of the same root cause (one responder starved of offers entirely, not an offer lost too fast).

## Priority table (interviews, tickets, and CSV data together)

| Problem area | Interviews | Tickets | CSV data (`callout-history.csv`) | Severity | Action needed |
|---|---|---|---|---|---|
| **Confirmed responder starvation** (Farlight, Meteor Mite, The Undertow, Vesper) | 1 of 4, indirectly (Kip) | 4 of 25 | **Yes** — 4 of 16 responders (25%) cut from ~12 offers/wk to 0-1, decelerating toward a floor with no bounce-back; see deep-dive below | Critical | **Now — fix** (routing / score-recovery change) |
| **Unexplained "gone quiet" reports** (9 other named responders) | 0 of 4 | 17 of 25 | **No** — these 9 responders' weekly `pings_sent` is flat or rising, contradicting the complaint | Unknown severity, but high distress (5 tickets use self-doubting language) | **Now — investigate** (push-notification-delivery hypothesis) |
| Timeout-driven near-misses on normal/busy responders | 3 of 4 (Ambrose, Dot, Halloran) | 8 of 25 | Yes — sent volume for most responders is *rising* post-4.2 (more offers, same 60s window), mechanically explaining more near-misses | Medium, expected tradeoff | **Now — decide** (keep 60s or dial back) |
| **Aggregate acceptance-rate "recovery" is partly illusory** | — | — | **Yes** — raw sent (165 vs. 172.3 baseline) and taken (120 vs. 132.3) are both still below pre-4.2 levels at 08-31, even though the rate climbed from 0.54 to 0.73; the rate recovers mainly because the four starved responders' offers stopped being sent at all | High — masks a real ongoing coverage shortfall | **Now — reframe the metric** (track total callouts placed and coverage gap, not rate alone) |
| Requisition approvals slow, no visibility | 1 of 4 (Halloran) | 0 of 25 — never escalated | N/A (Supply, not in this dataset) | High (safety gear) | **Now — fix**, and flag the ticket-detection gap |
| Status text/badges too small | 2 of 4 | — | N/A | Medium | Next |
| Notifications don't serve handlers | 2 of 4 | — | N/A | Medium | Next |
| No dark mode | 1 of 4 | — | N/A | Low, loud | Next |
| Filter persistence resets | 1 of 4 | — | N/A | Low | Next |
| Field failure reports vanish | 1 of 4 | — | N/A | Low | Next |
| Capability tag legend hard to find | 1 of 4 | — | N/A | Low | Later |
| Catalog search broken | 1 of 4 | — | N/A | Low | Later |

Four things changed from the last pass: the "starvation" bucket split into a confirmed fix and a separate open investigation once the ticket-to-CSV cross-check showed 17 of 21 "gone quiet" tickets don't match the data; the timeout bucket was demoted from "mystery" to "decision" since most of those tickets are the expected, understood cost of an intentional change; the requisition row carries its own flag, since zero tickets for the most severe complaint in the dataset means "ticket count" can't be trusted as a severity signal anywhere else in this table; and a new CSV-only row was added for the rate-recovery illusion, since neither the interviews nor the tickets could have surfaced it — it only shows up by looking at raw counts instead of the ratio.

## Grouped complaints (10 total, by how many of the 4 raised it)

| Complaint | Raised by | Count |
|---|---|---|
| Callouts vanish before responders can answer | Ambrose, Aunt Dot, Halloran | 3 of 4 |
| Status text/badges too small to read at a glance | Ambrose, Aunt Dot | 2 of 4 |
| Notifications don't serve handlers (no handler-side alert; indistinguishable sounds) | Aunt Dot, Kip | 2 of 4 |
| No dark mode | Kip | 1 of 4 |
| Filter persistence resets without warning | Ambrose | 1 of 4 |
| Capability tag legend hard to find | Ambrose | 1 of 4 |
| Requisition approvals slow, no visibility into why | Halloran | 1 of 4 |
| Field failure reports vanish with no feedback | Halloran | 1 of 4 |
| Equipment catalog search doesn't work | Halloran | 1 of 4 |
| Two responders, wildly different weeks, no explanation on screen | Kip | 1 of 4 |

## Quotes, one per complaint

- **Callouts vanish too fast** — "He comes down the stairs two at a time, and by the time he's actually got a thumb on the screen — it's gone." (Aunt Dot)
- **Text too small** — "At a glance I sometimes cannot tell engaged from available without leaning in." (Ambrose)
- **Notifications don't serve handlers** — "I want the alert sound to be different for each of them... both just go 'bing.'" (Kip)
- **No dark mode** — "It's 11pm... the console is just this wall of white light in the middle of my face. I am begging." (Kip)
- **Filter persistence unreliable** — "I'd rather it warned me the filter had reset than simply reset it." (Ambrose)
- **Capability tag legend hard to find** — "There was one in the spring I had to look up twice before it stuck." (Ambrose)
- **Requisition approvals slow** — "A real crack, not cosmetic — it sat waiting on a quartermaster signature for eleven days." (Halloran)
- **Field failure reports vanish** — "I file a failure report and it goes into a void. I'd like to know it did something." (Halloran)
- **Catalog search doesn't work** — "Typed 'plate,' got forty results, half of them unrelated." (Halloran)
- **Divergent responder patterns, unexplained** — "I'm looking at two cards on the same screen that might as well be two different products." (Kip)

## The one thing worth acting on first

Ambrose/Dot's "vanishing callout" complaint and Kip's "two heroes, two different weeks" observation read as separate issues but are almost certainly the same underlying routing problem, seen from two angles — corroborating evidence for the active 4.2 acceptance-rate investigation (see `CLAUDE.md`), not a new, separate fire.

---

## Support tickets (25 total)

### Grouped

| Group | Count | Description |
|---|---|---|
| Gone quiet — no offers at all | 16 of 25 | Ashgrove, Nightwell, The Undertow, Ironvale, Halfmoon, The Longcast, Stormwrack, Sgt. Falkirk, Farlight, The Drift |
| An offer came and vanished before they could react (standalone) | 4 of 25 | Captain Vantage, Sgt. Falkirk, The Longcast, Cindermark |
| Both at once — quiet for a while, then lost the one offer that finally came | 5 of 25 | Nightwell, The Undertow, Cindermark, The Drift, Ironvale |

### Quotes, one per group

- **Gone quiet** — "Nightwell's asked me twice now if her account is actually active, which it is, I've checked. I don't have a good answer for her at this point." (T-004, Marjorie Sung, Nightwell's handler)
- **Vanished before they could react** — "Almost had it. Literally had my thumb on the screen and it switched to someone else. Not happy." (T-015, Cindermark, responder)
- **Quiet, then lost it** — "First one in weeks and it vanished before i could even swipe. of course" (T-023, The Drift, responder)

### Filing-date pattern

Tickets run at roughly one per day from 13 Aug straight through 5 Sept with no decay — undercutting "seasonal, will recover in September" further than the CSV alone did (Nadia's own Slack read on 26 Aug, "not getting worse, not getting better," holds for the whole window).

The compound "quiet, then lost it" complaint (Group 3) only starts appearing after 24 August — but checked against the real per-responder data, only **one of the five** (The Undertow, T-019) is actually one of the four confirmed-collapsing responders. The other four (Nightwell, Cindermark, The Drift, Ironvale) have flat-or-rising ping volume in the CSV for the same weeks. Read: the compound complaint spread as a narrative pattern over time, not because more people were actually starving — people converged on a similar way of describing frustration the longer it circulated, independent of what their own numbers show.

### Other cuts worth running

- **Handler-filed vs. self-filed (mobile), and who has both.** 9 of 11 named individuals in the tickets have *both* a handler ticket and a responder-filed mobile ticket about the same quiet spell — near-universal two-voice corroboration (though not fully independent — handlers and responders talk to each other). More telling: **Meteor Mite and Vesper, two of the four confirmed-collapsing responders, have zero tickets at all**, from either side. The worst real cases never hit the support queue — we only know about them from Sofia's interviews.
- **Filer-assigned severity doesn't track the real cases.** Only one ticket in the set is marked "High" (T-019, The Undertow, a confirmed case) — the rest of the Medium/Low labels are scattered across both confirmed and mismatched cases with no pattern. Not a reliable triage signal on its own.
- **Explicit historical baseline vs. vague "it's been quiet."** A few tickets cite a specific comparison rather than a feeling: Ashgrove's handler calls him "normally one of our busier responders"; Ironvale's handler says nine days straight "has never happened... not since I've been handling her"; Stormwrack's handler says she "track[s] his week against last year's same week out of habit." Two of those three (Ashgrove, Stormwrack) are in the group whose CSV doesn't support the complaint — worth asking Ravi whether `callout-history.csv` is actually complete for every responder, rather than assuming the data automatically wins over a specific, tenured claim.
- **Repeat filers.** Three handlers escalated with a second ticket on the same responder — Marjorie Sung (Nightwell), Desmond Okafor (The Undertow), Teresa Alvarez (Ironvale) — each showing more resignation or higher stakes than their first. A support-process gap independent of root cause: filed once, got no resolution, came back.
- **Capability tag as a competing explanation, not yet ruled out.** The Undertow (aquatic) and Farlight (crowd-management) both carry niche tags. `WEIGHT_CAPABILITY_MATCH` didn't change in 4.2, so this is a weaker explanation than the routing-weight change, but it's still open — worth a one-line check with Ravi on incident volume by required capability tag, pre/post 4.2.

---

## Why the four confirmed responders have never recovered (CSV deep-dive)

The one number for Helen: **4 of 16 responders (25%) have been cut from ~12 offers a week to 0 or 1, three weeks after the release, with no sign of recovery.** Source: `00-rook/data/callout-history.csv`, comparing each responder's weekly `pings_sent` before and after 12 Aug.

Looking at the shape of the four curves, not just the endpoint, explains why "wait for September" won't fix this on its own:

- **The decline never has a good week.** Farlight 10→3→1→0, Meteor Mite 10→4→2→1, The Undertow 11→4→1→1, Vesper 12→5→2→1 — every week, for all four, independently, it only goes down or holds flat. That's the signature of a score with a hard floor and no way back up, matching the unresolved 2019 TODO in `history.py` about adding score recovery.
- **The drop comes in two stages.** A mild dip the first post-release week (08-10), then a 60–70% cliff the second week (08-17) for all four. That fits a compounding loop: the first week's declines/timeouts erode the recent-acceptance score just enough to fall out of contention under the heavier proximity weight, and once that happens they stop getting offered enough to ever earn it back.
- **These four were not chronically unreliable before 4.2 — the opposite, in three of four cases.** Pre-release acceptance rates: Farlight 0.74, Meteor Mite 0.69, The Undertow 0.78, Vesper 0.82 — Vesper's was one of the best on the whole roster, above the 0.77 group average. This rules out "these are just serial decliners" and instead matches the exact profile 4.2's stated rationale targeted: responders compensating for distance with strong acceptance history. The mechanism is working as redesigned, against a specific kind of responder who has no lever left to compensate with.
- **Even the rare offer they still get isn't landing.** By 08-24 and 08-31, all four are down to 1-2 offers/week, and every one goes unaccepted — consistent with them now only reaching the bottom of a long offer cascade (behind everyone who already declined or timed out), a second compounding effect on top of the ranking one.
- **No shared capability tag, no shared handler.** Undertow is aquatic, Farlight is crowd-management, and the other two are unstated — four different specialties and four different handlers (Linda Pruitt, Kip, Desmond Okafor, Aunt Dot) collapsing on the identical timeline. Weakens the "incident mix for a niche tag dried up" alternative and rules out a single handler or account-level issue.

Also worth flagging separately: the aggregate acceptance rate's "recovery" (0.54 → 0.73 by 08-31) is partly an illusion of composition, not genuine improvement. Both raw counts are still below the pre-4.2 baseline at 08-31 — sent 165 vs. 172.3, taken 120 vs. 132.3 — meaning Dispatch is still placing fewer callouts per week than before the release. The rate climbs mainly because the four collapsing responders' offers (which were dragging the rate down) have simply stopped being sent, not because the underlying problem improved. Worth asking Ravi for total callouts placed per week and the coverage-gap metric directly, not just the rate.

---

## Timing: when people wrote in vs. when the numbers actually moved

**People started writing in immediately.** T-001 is dated 13 Aug — one day after 4.2 shipped (12 Aug). Tickets then arrive at roughly one per day, without a gap, through 5 Sept.

**The numbers moved later, and in two steps.** The aggregate rate takes its first hit the week of 08-10 (0.77 → 0.54) — that week contains the release day. But the four confirmed responders only show a mild dip that first week (10-15%); the real collapse — the 60-70% cliff — doesn't happen until the week of **08-17**, five days after the release.

**Where tickets and data agree — a real lag, and an accurate one.** The two confirmed responders who actually have tickets show the data breaking *before* the complaint, not after. The Undertow's first ticket (T-005, 19 Aug: "one callout since the start of the month") lands inside the week his sent count fell from 11 to 4 (week of 08-17). Farlight's first ticket (T-018, 30 Aug: "almost two weeks without a single callout") backs out to roughly 17-18 Aug as the start of her quiet stretch — exactly when her own cliff happened. For these two, tickets are a lagging but accurate indicator.

**Where they disagree, and it's sharper than a magnitude mismatch.** T-002 (Corporal Ashgrove, filed 14 Aug) says his phone "hasn't gone off in six days" — putting the start of his quiet spell at roughly **8 August, four days before 4.2 even shipped**. That complaint cannot be caused by the release at all, by its own stated timeline, and Ashgrove's own data confirms it: his sent count in the release week is 10, identical to his pre-release baseline. Several of the other mismatched tickets (Nightwell's T-004, 18 Aug: "second week running") back out to similarly early or pre-release start dates, and none of their underlying numbers ever actually drop.

**Read:** the confirmed problem produces complaints that lag the real numbers by about a week — what you'd expect from something people notice after it's been going on a little while. The unconfirmed complaints lead the data, or predate the cause entirely, which looks much more like anxiety/contagion spreading through the roster than an independent, real signal from each person.

---

## Two stories, side by side: a confirmed case vs. an unconfirmed one

### Vesper (confirmed collapse)

| Week starting | Pinged | Took |
|---|---|---|
| 2026-06-29 | 14 | 11 |
| 2026-07-06 | 13 | 10 |
| 2026-07-13 | 15 | 13 |
| 2026-07-20 | 14 | 11 |
| 2026-07-27 | 13 | 11 |
| 2026-08-03 | 14 | 12 |
| 2026-08-10 | 12 | 6 |
| 2026-08-17 | 5 | 1 |
| 2026-08-24 | 2 | 0 |
| 2026-08-31 | 1 | 0 |

Six normal weeks (13-15 pinged, saying yes almost every time), then the release week shows a first crack (still 12 pings, but only half taken), then a genuine cliff: 5, then 2, then 1. In about three weeks, one of the busiest, most reliable responders on the roster goes from working almost daily to waiting a full week for a single call — and not getting even that one by the end.

### Corporal Ashgrove (originally "unconfirmed" — see the 5-agent investigation below, which found he may actually be an early-stage case of the same problem)

| Week starting | Pinged | Took |
|---|---|---|
| 2026-06-29 | 10 | 8 |
| 2026-07-06 | 11 | 9 |
| 2026-07-13 | 10 | 7 |
| 2026-07-20 | 9 | 7 |
| 2026-07-27 | 10 | 8 |
| 2026-08-03 | 10 | 8 |
| 2026-08-10 | 10 | 6 |
| 2026-08-17 | 8 | 5 |
| 2026-08-24 | 7 | 5 |
| 2026-08-31 | 7 | 5 |

His handler's ticket (T-002, filed 14 Aug) says his phone "hasn't gone off in six days" — six days back from the 14th lands on 8 Aug, *four days before 4.2 shipped*. The data backs that timing up in the worst possible way: his release-week ping count (10) is identical to his summer average, so nothing had happened yet when the complaint was filed. Over the following month he does get a little quieter — down to 7 pings a week from a ~10 average, roughly a 30% dip — but he never goes anywhere near zero, and he gets work every single week. Real, mildly annoying, and nowhere close to what the ticket describes.

Side by side, this is the clearest single illustration in the whole dataset of the difference between the confirmed problem and the unconfirmed one: one is a flatline; the other is a normal person having a slightly slower month, reported as a crisis. (Note: a later investigation, below, found Ashgrove's decline may be more than "just a slightly slower month" after all — see the gradient-check finding.)

---

## Five-agent investigation into root cause (28 Sept 2026)

Five agents each dug into one angle of the same question — what's actually driving the four-responder collapse — working independently from `callout-history.csv` and the routing code, then were compared against each other to see where they agreed, where they corrected the working theory, and what's still missing.

**Plain-language version:** They mostly agree on the big picture, but they caught a mistake in the earlier story, and found one new thing nobody had noticed yet. It's still true that the update made "how close are you" matter more and "how good is your recent record" matter less, and that once a responder starts missing jobs under the new rules there's no way built in for them to earn their way back — that part holds up. But the story that all four responders were "compensating for distance with a great track record" doesn't hold: one of them, Meteor Mite, actually had the *worst* acceptance rate on the whole team, not a great one. And two more responders — Corporal Ashgrove and Halfmoon — look like they're quietly sliding down the same path, just a few weeks behind, which nobody had flagged before this.

### What each agent found

1. **Score simulation** (rebuilt the routing engine's actual scoring math from real accept/decline counts): All four responders sat pinned near the maximum score for six weeks pre-4.2 — recent-acceptance was never their bottleneck. The score turns down the exact week 4.2 ships and hits or nears the floor (0.00–0.12) by 08-31 for all four, consistent with the missing score-recovery mechanism in `history.py`. **Wrinkle:** at the release week, ping volume had already started dropping while the simulated score was still 0.48–0.76 — nowhere near the floor. So the score collapse can't explain the *first* hit; something else (most likely the proximity-weight jump) does the initial damage, and the broken scoring compounds it afterward. Confidence: Medium.

2. **Gradient check** (tested whether it's really a clean 4-vs-12 split): It's not. It's a 3-tier pattern — 4 in freefall (-62% to -71%), **2 more (Corporal Ashgrove -20%, Halfmoon -18%) declining steadily and monotonically, below the dramatic threshold but real**, and 10 responders growing (+17% to +40%), with a genuine gap between the decliners and growers. Also found pre-4.2 acceptance rate does **not** predict who collapses — correlation is weak and wrong-signed. Vesper (82% acceptance, one of the best) collapsed; Meteor Mite (69%, the *worst* on the roster) also collapsed; The Drift (84%, similarly high to Vesper) grew instead. Neither acceptance rate nor prior volume cleanly separates the groups — the real discriminator is most likely geography/proximity, which isn't in this dataset. Confidence: Medium.

3. **Efficiency check** (system-wide "pings needed per successful placement"): Rose ~20% post-4.2 (1.30 → 1.56), and this isn't just the four collapsed responders — excluding them entirely, the other twelve still show a ~14% efficiency hit. The effect is front-loaded and slowly decaying (worst in the release week, tapering by 08-31) but hadn't fully returned to baseline by the end of the data. Confidence: Medium.

4. **Popularity / "rich get richer" check** (does pre-existing busyness predict outcome?): Decisively no. Vesper was the **2nd-busiest responder on the entire roster** pre-4.2 and collapsed to near-last; meanwhile several near-bottom responders pre-4.2 (The Drift, dead last; Ironvale, #14 of 16) surged into the middle of the pack. Prior rank predicts almost nothing outside the very top few, which rules out a generic momentum effect and points back to something orthogonal to popularity — consistent with proximity plus the broken recovery mechanism. Confidence: Medium-high.

5. **Consistency check** (is it always the same four at the bottom, or does it rotate?): Mostly stable, tightening toward perfectly stable. The four are the *exact* bottom four in 3 of the 4 post-4.2 weeks (missing only the release week itself, consistent with a mechanism that takes about a week to engage), with the gap to 5th place widening every week. Critically, **these four were never in the bottom four before 4.2** — they ran mid-pack to top-of-pack the entire pre-release period (Vesper was frequently 2nd or 3rd highest of all 16). A completely different, unrelated trio occupied the bottom before and after. This is a sharp reversal, not an acceleration of an existing weak spot. Confidence: High that this is structural and specific to these four, not random.

### Where they agree

- The collapse is real, release-triggered, and not random noise or rotation.
- It is not explained by a simple "popular gets more popular" effect (directly refuted).
- The routing-weight change (proximity up, recent-acceptance down) combined with the missing score-recovery mechanism is still the best-supported explanation for why it's permanent once it starts.
- It's independently corroborated by Sofia's interviews (Kip on Meteor Mite/The Gale, Aunt Dot on Vesper) — a completely separate data source lining up with the same names.

### Where they corrected the working theory

- **"High acceptance history compensating for distance" doesn't hold for all four.** Meteor Mite had the lowest acceptance rate on the entire roster, not a high one — so a strong track record isn't the common thread. The real shared trait is most likely pure geographic distance, unconfirmed because no location data exists in this dataset.
- **The four-responder scope may be six.** Corporal Ashgrove and Halfmoon show the same steady, monotonic, never-bouncing-back decline shape as the confirmed four did in their first two weeks — just earlier in the curve. Worth watching closely rather than writing off as "the nine unconfirmed" group.
- **Two separate mechanisms, not one.** The proximity-weight increase likely causes the initial drop in offers; the broken accept/decline scoring (no recovery function) is what makes it permanent. Conflating them into a single "the algorithm is broken" story oversimplifies which lever actually needs to move first.

### What's still needed to close the loop (agreed across agents)

1. **Actual location/travel-time data per responder** — the single most-repeated ask. Would directly confirm or kill the proximity hypothesis instead of inferring it.
2. **The real recent-acceptance score per responder per week**, as computed by the routing engine — not the hand-built approximation used here.
3. **Decline vs. timeout breakdown per event** — these may need different fixes and the CSV can't currently distinguish them.
4. **Incident volume and capability-tag mix by region over time** — to rule out "fewer nearby incidents" as a confound independent of ranking.
5. **A few more weeks of data** — to see whether Ashgrove/Halfmoon continue toward collapse or plateau, and whether system-wide efficiency fully recovers.
6. **Wen Li's confirmation** of how proximity and recent-acceptance actually combine into final rank — there's no written spec, and she's the only source of truth on it.

---

## How the code explains what the data showed

Read through `00-rook/code/dispatch-routing/` (availability.py, routing.py, history.py, offer.py, config.py) to connect the mechanism directly to the observed patterns, instead of just inferring it from the numbers.

**Why "far away" is a cliff, not a slope.** Proximity scoring gives a flat **zero** to anyone more than 45 minutes out (`PROXIMITY_HORIZON_MINUTES` in `config.py`) — no partial credit past that line. This is consistent with the collapsed responders hitting a wall rather than a gradual decline once they crossed some distance threshold, and it's the direct reason location/travel-time data (still missing) would settle the proximity question outright.

**Why the break was instant and system-wide.** The proximity/recent-acceptance weights and the offer timeout are single config values (`config.py`) applied to every ranking the moment they change — there's no rollout curve. That matches the sharp, same-week break in the CSV rather than a gradual seasonal slide.

**Why the collapse never reverses on its own.** The recent-acceptance score (`history.py`) only moves down on a decline *or* a timeout (identical penalty, no distinction) and has no function to drift back up over time — an unresolved 2019 TODO in the same file. Once a responder's score is knocked down and they stop being offered work, there's no way to earn it back, because earning it back requires being offered work. This is the mechanical explanation for "the decline never has a good week" in the four (now possibly six) responders' data.

**Why Meteor Mite broke the "great acceptance history" theory but still collapsed just as hard.** If her recent-acceptance score was already below-neutral before 4.2 (her pre-release acceptance rate was the lowest on the roster), she wasn't relying on a strong score to offset distance the way the original theory assumed — she may simply have been another far-away responder with nothing protecting her at all. This reframes the four (or six) as probably united by distance first, with their pre-existing acceptance score only determining how fast each one hit the floor, not whether they were affected.

**Why nearly everyone, not just the four, started losing offers "too fast to answer."** Every responder gets the same fixed answer window (`offer.py`, driven by `OFFER_TIMEOUT_SECONDS` in `config.py`), cut from 90s to 60s in 4.2. A shorter window mechanically produces more timeouts across the whole roster, independent of the starvation mechanism — this is the system-wide "vanished before I could respond" pattern seen in most tickets, not just the four/six.

**Why the system needs more pings per successful placement now.** `offer.py` walks the ranked list one responder at a time until someone accepts; a shorter timeout raises the odds of a "no answer" at each stop, which lengthens the average cascade before a job gets filled. This is the direct mechanical cause of the ~20% efficiency drop found in the data.

**Why the aggregate acceptance rate looks like it's recovering.** Nothing in the code formally excludes a responder — `routing.py`'s own comment says "everyone available is on the list" — but a responder with a zero proximity score and a floored acceptance score will almost never be reached before someone else on the list accepts first. They're never technically banned, just never practically reached. Once Rook stops effectively asking its worst-performing responders, the average "yes rate" for everyone else looks better — not because anything improved, but because the low-performing offers driving the rate down simply stopped happening.

### TL;DR — what to do next
1. Get real location/travel-time data for all 16 responders — the single biggest missing piece, would directly confirm or kill the proximity theory.
2. Get the real recent-acceptance score from Ravi (not the hand-built approximation) plus a decline-vs-timeout breakdown per event.
3. Get 20 minutes with Wen Li on how proximity and reliability combine, and specifically raise adding a score-recovery mechanism — the most likely real fix, not reverting the release.
4. Watch Corporal Ashgrove and Halfmoon for a few more weeks — they may be the same problem, a few weeks behind.
5. Take the 60-second timeout to Helen as its own decision (keep vs. dial back) — it's a tradeoff, not a mystery.
6. Don't touch the routing weights yet — wait for the location data and Wen's read first.

One concrete clue already in hand, worth raising directly with Wen or Marcus: Kip's interview states Meteor Mite and The Gale are in the **same city**, yet one collapsed and the other is thriving — a direct complication for the proximity theory as applied to her specifically, even though it likely still holds for the other three.

---

## Hypotheses to test, ranked by likelihood of resolving root cause

| # | Hypothesis | If / Then / Because | Confirms if | Fails if | Likelihood of resolving |
|---|---|---|---|---|---|
| 1 | Score-recovery | **If** the recent-acceptance score has no mechanism to recover over time, **then** responders who hit the score floor will show flat-or-zero offer volume indefinitely, **because** the system penalizes every decline/timeout without ever restoring the score | Real score data sits at or near 0.0 for the full window, with no upward movement in any week | Real scores show periodic recovery — e.g., drifting back toward 0.5 after a dip | Very high |
| 2 | Proximity | **If** distance to incidents is the primary driver of the collapse, **then** responders farther from incident clusters will show lower offer volume post-4.2, **because** proximity now counts for 60% of ranking instead of 45% | Location/travel-time data shows the affected responders are measurably farther from incident concentrations than the growing group | The affected responders aren't meaningfully farther away (consistent with the Meteor Mite/The Gale same-city finding) | High (one known exception) |
| 3 | Timeout mechanics | **If** the shortened 60-second window is driving widespread "vanished too fast" complaints, **then** timeout-specific events will rise broadly across the whole roster post-4.2, **because** everyone gets less time to respond regardless of who they are | Timeout rates rise broadly, independent of a responder's score or location | Timeout rates don't meaningfully change, or complaints trace back to active declines instead | High |
| 4 | Notification failure | **If** the 9 unexplained "quiet" complaints are a delivery failure rather than a real drop in offers, **then** push-notification logs for those 9 will show reduced delivery success during their complaint window, **because** the offer would be generated but never reach the device | Delivery success for these 9 is measurably lower than the rest of the roster in that window | Their delivery rates look normal — pointing to perception/contagion instead | Medium |
| 5 | Capability mismatch (Meteor Mite) | **If** her collapse is a tag mismatch rather than distance, **then** incident volume requiring her specific tag will drop starting mid-August, **because** fewer matching incidents would reduce her offers independent of ranking | Incident volume for her tag(s) drops in step with her ping-volume collapse | Incident volume for her tag(s) stayed flat or rose | Medium |
| 6 | Early-stage collapse (Ashgrove & Halfmoon) | **If** they're early-stage cases of the same mechanism, **then** their weekly offer volume will keep declining monotonically toward zero, **because** they'd be following the same two-stage curve already observed | Their numbers keep sliding with no bounce-back over the next 2-3 weeks | Their numbers stabilize or recover on their own | Low (needs time to pass) |

**Recommendation:** prioritize #1 and #2 together — they cover the full causal chain (proximity as the likely trigger, broken score-recovery as why it never lets go), both are resolvable with a single data pull or conversation rather than weeks of waiting, and both are backed by evidence already in hand: the hand-simulated score hit the literal floor (0.00) for three of four responders by 08-31, and the same four were the exact bottom-four responders in 3 of 4 post-4.2 weeks despite never being near the bottom before the release.
