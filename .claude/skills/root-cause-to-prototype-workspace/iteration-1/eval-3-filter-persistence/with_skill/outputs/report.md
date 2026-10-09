No mockup/prototype file was created, and that's a deliberate conclusion, not an oversight — see below.

---

# Investigation: "The console filter-persistence bug is causing complaints"

**Scope:** Rook Industries dispatch/callout complaints, Aug–Sep 2026. Sources read in full: all 25 tickets (`00-rook/feedback/tickets/t-001.txt`–`t-025.txt`), all 4 research interviews (`00-rook/feedback/interviews/ambrose.txt`, `aunt-dot.txt`, `halloran.txt`, `kip.txt`), plus `00-rook/code/dispatch-routing/` (CHANGELOG.md, config.py, offer.py, routing.py), `00-rook/data/callout-history.csv`, and `00-rook/company/notes/dispatch-slack-thread.txt`.

## What I did
1. Read every ticket and interview transcript in full (not a sample), tagging each complaint by symptom.
2. Checked the dispatch-routing codebase's changelog and config to see what actually shipped in the release the complaints cluster around.
3. Cross-referenced ticket dates and interview quotes against the engineering team's own Slack thread from the same period.
4. Pulled `callout-history.csv` and computed weekly accept rate and per-responder variance before/after the release, to test the theory against data the tickets/interviews didn't generate themselves.

## What the evidence actually shows: NOT SUPPORTED

The filter-persistence theory looked plausible only because it shares a release date with the real cause. Every independent source points elsewhere.

- `CHANGELOG.md` 4.2 (12 Aug 2026) bundled three unrelated changes in one release: (1) console filter persistence, explicitly annotated **"not in this service"** — i.e. a frontend-only change with no code path into dispatch/offers; (2) offer timeout cut from 90s to 60s (`config.py`); (3) ranking weights rebalanced — `WEIGHT_PROXIMITY` 0.45→0.60, `WEIGHT_RECENT_ACCEPTANCE` 0.40→0.25.
- All dated tickets start 13 Aug 2026 (day after release) and split into two clusters: "offer vanished before I could answer" (T-001, T-003, T-007, T-011, T-015, T-019, T-020, T-023, T-025) and "nothing's come in for ages" (T-002, T-004, T-005, T-008, T-009, T-010, T-012, T-013, T-014, T-016, T-017, T-018, T-021, T-022, T-024). None mention filters or saved views.
- Interviews actively rule out the filter theory:
  - **Ambrose** is the one heavy filter user and praises the filter-persistence fix outright; he raises the missed-callout incident as an explicitly *separate* topic, and independently describes the proximity/acceptance-weight symptom from the outside ("a slower-arriving response... lately that doesn't seem to hold").
  - **Halloran** reports the same near-miss symptom for Bulwark but never uses filters — "straight to the profile, always." Symptom persists with zero filter exposure.
  - **Kip** reports the clearest feast-or-famine pattern (Meteor Mite dead quiet, The Gale nonstop, same week/city) while explicitly saying he "barely uses" filters.
  - **Aunt Dot** independently describes both the fast-loss and quiet-stretch patterns without mentioning filters at all.
- The Slack thread (`dispatch-slack-thread.txt`) shows the dispatch team reaching the identical split in real time (18 Aug): "phone never even goes off anymore" vs. "gone before they've got a thumb on the screen." Nadia Hoffmann attributes the second directly to the timeout cut. Marcus Oyelaran separately flags (14 Aug) that the weight rebalance doesn't distinguish responders who'd been declining jobs from everyone else — and nobody ever answers that question (Wen Li on PTO; Priya left 21 Aug).
- Data confirms a step-change, not a coincidence or seasonal drift:
  - Weekly accept rate: steady ~0.75–0.78 for six pre-release weeks, drops to **0.54** the release week (2026-08-10), recovers only to ~0.73 three weeks later. A one-week cliff, not a seasonal fade (contra Priya's seasonality theory from the Slack thread).
  - Per-responder weekly offer-count std dev roughly **doubles** post-release (2.46 → 6.11) while the mean barely moves (10.77 → 10.10) — total work didn't shrink, it got redistributed, exactly matching Kip's "two cards, same week, same city, totally different stories."

**Bottom line:** the real cause is the 4.2 routing-engine change (shorter offer timeout + proximity-up/recent-acceptance-down weight rebalance), not the console filter-persistence feature, which has no code path into offer dispatch and whose heaviest user (Ambrose) is unaffected by the offer-timing bug it's being blamed for.

## Falsifiable hypotheses

| # | Hypothesis | Confirms if | Fails if | Data needed | Resolvable how soon |
|---|---|---|---|---|---|
| 1 | Shortened offer window (90s→60s) causes the missed-offer complaints. | Missed-offer tickets cluster right after 12 Aug, describe very short windows. | Tickets predate 12 Aug or describe windows well over 60s. | Already have it | Now — confirmed |
| 2 | Weight rebalance (proximity up, recent-acceptance down) causes the quiet-stretch complaints. | Per-responder offer variance rises post-release with flat total volume; quiet responders skew toward lower recent-acceptance/farther proximity. | Variance flat, or quiet responders random w.r.t. proximity/acceptance. | Already have it | Now — confirmed |
| 3 | Console filter persistence is unrelated to either symptom. | Symptoms appear regardless of a handler's filter usage. | Symptoms correlate specifically with filter use/config. | Already have it | Now — confirmed; theory rejected |
| 4 | The two clusters are one compounding mechanism, not two bugs, and can hit the same account in sequence. | Same responder shows quiet-then-lost back to back. | No account shows both. | Already have it | Now — confirmed: Ironvale (T-008 quiet → T-025 quiet-then-lost), The Undertow (T-005 quiet → T-019 quiet-then-lost) |

## Named gap (what's still unverified)
- Marcus's 14 Aug Slack question — whether the recent-acceptance weight cut was meant to target only responders who'd been declining jobs, or landed on everyone "because the config doesn't distinguish" — was never answered. This matters: intentional vs. accidental changes what "the fix" means. Owner: whoever now owns `config.py` (Wen Li, per the thread).
- `callout-history.csv` is weekly aggregates, not per-offer timestamps, so the "a few seconds" framing in interviews is anecdotal, not measured. A raw offer/response-timestamp pull would make hypothesis 1 precise.
- I haven't independently verified Nadia's reported ~2:1 "quiet vs. lost" ticket split beyond my own tagging (mine came out ~15:9 among dated tickets, roughly consistent but not identical — worth reconciling against her underlying count if it matters for prioritization).

## Mock-up decision
No prototype was built. Per the task brief, if the evidence doesn't support the theory I should say so rather than build anyway — and it doesn't. A console filter mock-up would solve a problem that isn't occurring, and could put the (valued, working) filter-persistence feature at risk of being reworked or rolled back for the wrong reason. If a prototype is wanted next, the right one is a small interactive model of the ranking formula (sliders for the three weights + timeout, replayed against real profiles like Ironvale's or The Undertow's) rather than anything console/UI-facing — I did not build this since it wasn't asked for and building was explicitly conditional on the theory holding up.

---

## Final response, as delivered to the user

I dug through all 25 tickets, all 4 interviews, the dispatch-routing code and changelog, the team's own Slack thread from when this started, and the callout-history data. Short version: **the filter-persistence theory doesn't hold up — I'd drop it.**

The console filter-persistence fix is a frontend-only change (the changelog literally tags it "not in this service" — no code path into dispatch or offers), and the person who actually uses and likes it (Ambrose) reports the missed-callout problem as a separate issue entirely. Meanwhile the same symptoms — offers vanishing instantly, and long dead stretches — show up just as badly for handlers who never touch filters (Halloran goes straight to a profile page; Kip "barely uses" filters at all) and don't track with filter usage anywhere in the data.

What's actually going on: the same release that shipped the filter fix also shipped two routing-engine changes — the offer response window got cut from 90 seconds to 60, and the ranking formula shifted to weight proximity more and recent-acceptance history less. Both land on the exact date the tickets start, and both show up in the numbers: weekly accept rate drops from a steady ~77% to 54% the release week and only climbs back to ~73% three weeks later, and the spread in how many offers each responder gets roughly doubles. That's the "gone before I could answer" cluster and the "my phone hasn't gone off in 10 days" cluster — and a couple of accounts (Ironvale, The Undertow) show both hitting back to back.

This actually matches what your own team said in real time on Slack — Nadia pinned the fast-loss complaints on the timeout cut the same week, and Marcus asked whether the weight change was meant to hit only responders who'd been declining jobs, a question that never got answered before the PTO/departure handoff. Priya's instinct that August is "always a little soft" is a fair prior, but a one-week cliff isn't what a seasonal dip looks like.

Since the suspected cause didn't check out, I didn't build a console mock-up — that would solve the wrong problem. I'd suggest instead: test reverting or softening the offer timeout and the weight rebalance (start with something between 60s and the old 90s, watch whether accept rate recovers), and get a straight answer on whether the recent-acceptance penalty was meant to apply only to people who'd been declining, since that changes what the fix looks like. Happy to build a small interactive model of the ranking formula against real responder profiles if that'd help you see the mechanism — just say so.
