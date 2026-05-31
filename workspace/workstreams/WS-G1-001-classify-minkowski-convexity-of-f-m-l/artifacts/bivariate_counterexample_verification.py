from __future__ import annotations

import sympy as sp


def main() -> None:
    x, y, d = sp.symbols("x y d", positive=True, integer=True)
    f4 = 3 * (x + y) ** 4 - 2 * x**4 - 2 * y**4

    for m, point in [(2, (2, 1)), (3, (4, 1))]:
        quotient = sp.diff(f4, y, m) / sp.diff(f4, y, 1)
        hessian = sp.simplify(sp.hessian(quotient, (x, y)).subs({x: point[0], y: point[1]}))
        print(f"N=4, m={m}, point={point}")
        print(f"Hessian={hessian}")
        print(f"det={sp.factor(hessian.det())}")
        print(f"trace={sp.factor(hessian.trace())}")
        print()

    s = sp.symbols("s", positive=True)
    quotient_q1 = (3 * s - 2 * y) / (3 * s**d - 2 * y**d)
    determinant = sp.factor(sp.hessian(quotient_q1, (s, y)).det().subs({s: 3, y: 1}))
    print("General q=1 determinant at (s,y)=(3,1):")
    print(determinant)


if __name__ == "__main__":
    main()
