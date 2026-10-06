"""Replay real weekly callout data under the current scoring rule and two recovery rules.

Score-only simulation. It does not model offer volume, since we have no proximity data.
Weekly approximation: taken = accepted events, (sent - taken) = declined/timed-out events.
"""

import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "00-rook" / "data" / "callout-history.csv"

NEUTRAL = 0.5
CREDIT = 0.08
PENALTY = 0.12
FLOOR = 0.0
CEILING = 1.0
DRIFT = 0.10

CONFIRMED = ["Farlight", "Meteor Mite", "The Undertow", "Vesper"]
WATCH = ["Corporal Ashgrove", "Halfmoon"]


def clamp(v):
    return max(FLOOR, min(CEILING, v))


def step_current(score, sent, taken):
    return clamp(score + taken * CREDIT - (sent - taken) * PENALTY)


def step_drift(score, sent, taken):
    score = step_current(score, sent, taken)
    return clamp(score + DRIFT * (NEUTRAL - score))


def step_rest_drift(score, sent, taken):
    score = step_current(score, sent, taken)
    if sent <= 1:
        return clamp(score + DRIFT * (NEUTRAL - score))
    return score


TIMEOUT_SHARE = 0.5
TIMEOUT_PENALTY = PENALTY / 2


def step_timeout_half(score, sent, taken):
    misses = sent - taken
    timeouts = misses * TIMEOUT_SHARE
    declines = misses - timeouts
    penalty = declines * PENALTY + timeouts * TIMEOUT_PENALTY
    return clamp(score + taken * CREDIT - penalty)


RULES = {
    "current": step_current,
    "drift every week": step_drift,
    "drift in quiet weeks only": step_rest_drift,
    "timeouts count half": step_timeout_half,
}


def load_weeks():
    weeks = defaultdict(dict)
    with DATA.open() as f:
        for row in csv.DictReader(f):
            weeks[row["responder"]][row["week_starting"]] = (
                int(row["pings_sent"]),
                int(row["pings_taken"]),
            )
    return weeks


def trajectory(events, step):
    score = NEUTRAL
    out = []
    for sent, taken in events:
        score = step(score, sent, taken)
        out.append(score)
    return out


def main():
    weeks = load_weeks()
    dates = sorted({d for r in weeks.values() for d in r})

    print("Score at end of data (2026-08-31), by rule")
    print(f"{'responder':<20}" + "".join(f"{name:>26}" for name in RULES))
    for name in CONFIRMED + WATCH:
        events = [weeks[name][d] for d in dates]
        finals = [trajectory(events, step)[-1] for step in RULES.values()]
        print(f"{name:<20}" + "".join(f"{v:>26.2f}" for v in finals))

    print()
    print("Decliner test: a responder who gets 10 offers a week and says no to all of them, for 10 weeks")
    decliner = [(10, 0)] * 10
    for name, step in RULES.items():
        traj = trajectory(decliner, step)
        print(f"  {name:<26} week 1: {traj[0]:.2f}   week 10: {traj[-1]:.2f}")

    print()
    print("Reading: a total refuser stays near the floor under every rule. Drift lifts them to 0.05 and the")
    print("weekly penalty pushes them back down, so drift alone is too weak to rescue a responder who keeps refusing.")


if __name__ == "__main__":
    main()
