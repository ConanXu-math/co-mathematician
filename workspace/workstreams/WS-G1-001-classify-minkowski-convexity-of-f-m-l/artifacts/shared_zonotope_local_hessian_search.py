from __future__ import annotations

import itertools

import numpy as np

SEED = 2026053003


def build_terms(
    n: int, generator_count: int, k_from_k_body: int, directions: np.ndarray, l_lengths: np.ndarray
) -> list[tuple[float, tuple[int, ...]]]:
    """Terms of V(K[k], L[n-k]) for zonotopes sharing fixed directions."""
    terms: list[tuple[float, tuple[int, ...]]] = []

    for selected in itertools.combinations(range(generator_count), n):
        determinant_weight = abs(np.linalg.det(directions[list(selected), :].T))
        if determinant_weight < 1e-12:
            continue

        selected_set = set(selected)
        for k_indices in itertools.combinations(selected_set, k_from_k_body):
            k_set = set(k_indices)
            coefficient = determinant_weight
            for index in selected_set - k_set:
                coefficient *= l_lengths[index]
            terms.append((coefficient, tuple(sorted(k_set))))

    return terms


def evaluate_squarefree_terms(
    terms: list[tuple[float, tuple[int, ...]]], x_lengths: np.ndarray
) -> tuple[float, np.ndarray, np.ndarray]:
    value = 0.0
    gradient = np.zeros_like(x_lengths)
    hessian = np.zeros((len(x_lengths), len(x_lengths)))

    for coefficient, indices in terms:
        monomial = coefficient
        for index in indices:
            monomial *= x_lengths[index]

        value += monomial

        for index in indices:
            gradient[index] += monomial / x_lengths[index]

        for position, first in enumerate(indices):
            for second in indices[position + 1 :]:
                entry = monomial / (x_lengths[first] * x_lengths[second])
                hessian[first, second] += entry
                hessian[second, first] += entry

    return value, gradient, hessian


def quotient_hessian(
    n: int,
    generator_count: int,
    m: int,
    directions: np.ndarray,
    l_lengths: np.ndarray,
    x_lengths: np.ndarray,
) -> tuple[float, np.ndarray]:
    """Return F and its Hessian in the shared-direction zonotope length cone."""
    numerator_terms = build_terms(n, generator_count, n - m, directions, l_lengths)
    denominator_terms = build_terms(n, generator_count, n - 1, directions, l_lengths)

    numerator, numerator_gradient, numerator_hessian = evaluate_squarefree_terms(
        numerator_terms, x_lengths
    )
    denominator, denominator_gradient, denominator_hessian = evaluate_squarefree_terms(
        denominator_terms, x_lengths
    )

    hessian = (
        numerator_hessian / denominator
        - np.outer(numerator_gradient, denominator_gradient) / denominator**2
        - np.outer(denominator_gradient, numerator_gradient) / denominator**2
        - numerator * denominator_hessian / denominator**2
        + 2 * numerator * np.outer(denominator_gradient, denominator_gradient) / denominator**3
    )

    return numerator / denominator, (hessian + hessian.T) / 2


def run_search() -> list[str]:
    rng = np.random.default_rng(SEED)
    cases = [(4, 7, 2000), (4, 9, 1000), (5, 8, 500)]
    lines = [f"Random seed: {SEED}", "Shared-direction zonotope local Hessian search:"]

    for n, generator_count, trials in cases:
        found_violation = False
        best_min_eigenvalue = float("inf")
        best_context: tuple[int, int, float] | None = None

        for trial in range(trials):
            directions = rng.normal(size=(generator_count, n))
            l_lengths = np.exp(rng.normal(0.0, 1.0, size=generator_count))
            x_lengths = np.exp(rng.normal(0.0, 1.0, size=generator_count))

            for m in range(2, n):
                value, hessian = quotient_hessian(
                    n, generator_count, m, directions, l_lengths, x_lengths
                )
                min_eigenvalue = float(np.linalg.eigvalsh(hessian)[0])
                if min_eigenvalue < best_min_eigenvalue:
                    best_min_eigenvalue = min_eigenvalue
                    best_context = (trial, m, float(value))

                if min_eigenvalue < -1e-8:
                    lines.append(
                        "violation "
                        f"n={n} generators={generator_count} trial={trial} m={m} "
                        f"min_eigenvalue={min_eigenvalue:.12g} F={value:.12g}"
                    )
                    found_violation = True
                    break

            if found_violation:
                break

        lines.append(
            f"n={n}, generators={generator_count}, trials={trials}, "
            f"violation_found={found_violation}, "
            f"best_min_eigenvalue={best_min_eigenvalue:.12g}, "
            f"best_context={best_context}"
        )

    return lines


if __name__ == "__main__":
    for output_line in run_search():
        print(output_line, flush=True)
