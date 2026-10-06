"""SYNTHETIC DATA. Not real responder behavior.

The real weekly data does not say how many misses were timeouts versus active declines.
This script fills that gap with random splits drawn from an assumed range, runs the same
score rules as recovery_simulation.py, and reports how much the outcome moves across splits.

Nothing here is evidence about real responders. It only measures how sensitive the
simulated result is to the missing timeout split.
"""

import random
import statistics

import recovery_simulation as sim

SEEDS = 500
TIMEOUT_SHARE_RANGE = (0.2, 0.8)
TIMEOUT_RATIO = 0.5
DRIFT = 0.10


def synthetic_share(rng):
    return rng.uniform(*TIMEOUT_SHARE_RANGE)


def run_rule(events, shares, use_softer, use_drift):
    score = sim.NEUTRAL
    for (sent, taken), share in zip(events, shares):
        misses = sent - taken
        timeouts = misses * share if use_softer else 0.0
        declines = misses - timeouts
        penalty = declines * sim.PENALTY + timeouts * sim.PENALTY * TIMEOUT_RATIO
        if not use_softer:
            penalty = misses * sim.PENALTY
        score = sim.clamp(score + taken * sim.CREDIT - penalty)
        if use_drift:
            score = sim.clamp(score + DRIFT * (sim.NEUTRAL - score))
    return score


def percentile(values, p):
    ordered = sorted(values)
    k = (len(ordered) - 1) * p
    lo, hi = int(k), min(int(k) + 1, len(ordered) - 1)
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (k - lo)


def main():
    weeks = sim.load_weeks()
    dates = sorted({d for r in weeks.values() for d in r})
    names = sim.CONFIRMED + sim.WATCH
    rules = {
        "today's rules": (False, False),
        "only bounce back": (False, True),
        "only softer timeouts": (True, False),
        "both": (True, True),
    }

    print("SYNTHETIC: random timeout splits, 500 runs each. End-of-August score, median (10th-90th percentile)")
    print(f"{'hero':<20}" + "".join(f"{r:>26}" for r in rules))
    for name in names:
        events = [weeks[name][d] for d in dates]
        row = []
        for use_softer, use_drift in rules.values():
            finals = []
            for seed in range(SEEDS):
                rng = random.Random(f"{name}-{seed}")
                shares = [synthetic_share(rng) for _ in events]
                finals.append(run_rule(events, shares, use_softer, use_drift))
            med = statistics.median(finals)
            lo, hi = percentile(finals, 0.1), percentile(finals, 0.9)
            row.append(f"{med:.2f} ({lo:.2f}-{hi:.2f})")
        print(f"{name:<20}" + "".join(f"{c:>26}" for c in row))

    print()
    print("Read: the spread shows how much the answer depends on the missing timeout split.")
    print("A wide spread means the real split needs measuring before we trust any single number.")


if __name__ == "__main__":
    main()
