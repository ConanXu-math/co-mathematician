from __future__ import annotations

import itertools
import math
import random

SEED = 20260530


def mixed_box_volume(a: list[float], b: list[float], m: int) -> float:
    """Mixed volume V(Box(a)[n-m], Box(b)[m]) for axis-aligned boxes."""
    n = len(a)
    total = 0.0
    for selected in itertools.combinations(range(n), m):
        selected = set(selected)
        product = 1.0
        for i in range(n):
            product *= b[i] if i in selected else a[i]
        total += product
    return total / math.comb(n, m)


def F(a: list[float], b: list[float], m: int) -> float:
    return mixed_box_volume(a, b, m) / mixed_box_volume(a, b, 1)


def explicit_m0_violation(n: int, R: float) -> tuple[float, float]:
    b = [1.0] * n
    a0 = [R, 1.0] + [1.0] * (n - 2)
    a1 = [1.0, R] + [1.0] * (n - 2)
    amid = [(x + y) / 2.0 for x, y in zip(a0, a1)]
    midpoint = F(amid, b, 0)
    endpoint_average = (F(a0, b, 0) + F(a1, b, 0)) / 2.0
    return midpoint, endpoint_average


def randomized_midpoint_search(
    n: int, m: int, rng: random.Random, trials: int = 5000
) -> bool:
    b = [rng.uniform(0.2, 3.0) for _ in range(n)]
    for _ in range(trials):
        a0 = [rng.uniform(0.2, 3.0) for _ in range(n)]
        a1 = [rng.uniform(0.2, 3.0) for _ in range(n)]
        amid = [(x + y) / 2.0 for x, y in zip(a0, a1)]
        if F(amid, b, m) > (F(a0, b, m) + F(a1, b, m)) / 2.0 + 1e-10:
            return True
    return False


if __name__ == "__main__":
    rng = random.Random(SEED)
    print(f"Random seed: {SEED}")
    print()
    print("Explicit m=0 violations with R=2:")
    for n in range(2, 8):
        midpoint, endpoint_average = explicit_m0_violation(n, 2.0)
        print(
            f"n={n}: F(midpoint)={midpoint:.12f}, "
            f"endpoint average={endpoint_average:.12f}, "
            f"violation={midpoint > endpoint_average}"
        )

    print("\nRandom box midpoint search:")
    for n in range(2, 7):
        outcomes = []
        for m in range(0, n + 1):
            outcomes.append((m, randomized_midpoint_search(n, m, rng)))
        print(f"n={n}: {outcomes}")
