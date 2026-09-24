# Ravi 1:1 — Dispatch Acceptance Rate

23 September 2026 · Faran · 30 min

**Purpose:** Get real per-responder numbers before taking a position with Helen or the team on what's actually happening with 4.2. The aggregate weekly rate (0.78 → 0.54 → recovering) is hiding a pattern I want confirmed or ruled out before I act on it.

## 1. Level-set (5 min)

- I've seen the rough weekly acceptance-rate numbers Marcus pulled and the callout-history data in the repo. I want the real numbers — is there a reason the two would differ meaningfully?
- How far back does clean data actually go? I want to check the "August is always soft, every year" claim from Priya's handoff against last year — can we pull that?

## 2. Test the concentration theory (core of the meeting)

- When I split the data by responder instead of aggregating, four of them — Farlight, Meteor Mite, The Undertow, Vesper — go from ~10-14 offers/week to 0-1 by end of August, while most of the other twelve are getting *more* offers than before 4.2. Does that hold up in your source of truth, or is that an artifact of whatever export I was looking at?
- If it holds: is there anything those four have in common — region, capability tags, tenure — that the rest don't? Need to rule out "these four just have niche capability tags and incident mix changed" before pointing at the routing weights.
- Can you pull the same per-responder weekly view for the other nine who've filed "gone quiet" tickets (Ashgrove, Nightwell, Ironvale, Halfmoon, The Longcast, Falkirk, Stormwrack, Cindermark, The Drift)? My read of the weekly aggregate says their volume is flat or rising, which contradicts their tickets — is that real or am I missing granularity?

## 3. Granularity gap

- Everything I've seen is weekly aggregate (pings_sent / pings_taken). Do we have anything at the offer/event level — timestamp per offer, accepted/declined/timed-out as separate outcomes? That's the only way to tell whether the nine "quiet" complaints are real within-week dead spells or just weekly noise.
- Does your data distinguish an active decline from a timeout, or are they collapsed into one outcome the way they appear to be in the routing code?

## 4. Recent-acceptance score visibility

- Is the actual recent-acceptance score (the 0–1 value routing uses) something you can see per responder, or only the resulting offer counts? Want to check whether the four collapsing responders are sitting at the score floor, which would confirm the mechanism rather than just the symptom.

## 5. Close

- What's the fastest way to get a standing view of this split by responder, not just the weekly aggregate — a saved query, a dashboard, something in #data?
- Given what we look at today, does "recovering, mostly seasonal" still look right, or does it change how this should be characterized before I talk to Helen?

---

**What I want to walk out with:** confirmation (or not) that this is a concentrated ~4-responder problem rather than a broad softening, and whether I have — or can get — the event-level data to settle the other nine tickets one way or the other.
