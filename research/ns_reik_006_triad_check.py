#!/usr/bin/env python3
"""Finite exact 4^3-grid checks for NS-REIK-006; Python standard library only."""
from fractions import Fraction
from itertools import product

K = ((1, 0, 0), (0, 1, 1), (1, 1, 1))
A = ((0, -2, 2), (1, -2, 2), (1, 1, -2))
SIN, COS = (0, 1, 0, -1), (1, 0, -1, 0)


def evaluate(amplitudes):
    total = dict(K=0, E=0, D=0, S=0)
    for xyz in product(range(4), repeat=3):
        u = [0] * 3
        grad = [[0] * 3 for _ in range(3)]
        hess = [[[0] * 3 for _ in range(3)] for _ in range(3)]
        for wave, (amp, k, a) in enumerate(zip(amplitudes, K, A)):
            p = sum(k[j] * xyz[j] for j in range(3)) % 4
            f = SIN[p] if wave == 0 else COS[p]
            fp = COS[p] if wave == 0 else -SIN[p]
            for i in range(3):
                u[i] += amp * a[i] * f
                for j in range(3):
                    grad[i][j] += amp * a[i] * k[j] * fp
                    for h in range(3):
                        hess[i][j][h] -= amp * a[i] * k[j] * k[h] * f
        w = (grad[2][1] - grad[1][2],
             grad[0][2] - grad[2][0],
             grad[1][0] - grad[0][1])
        dw = [[hess[2][1][j] - hess[1][2][j] for j in range(3)],
              [hess[0][2][j] - hess[2][0][j] for j in range(3)],
              [hess[1][0][j] - hess[0][1][j] for j in range(3)]]
        total['K'] += sum(v*v for v in u)
        total['E'] += sum(v*v for v in w)
        total['D'] += sum(dw[i][j]**2 for i in range(3) for j in range(3))
        total['S'] += sum(w[i] * grad[i][j] * w[j]
                          for i in range(3) for j in range(3))
    return {key: Fraction(val, 64) for key, val in total.items()}


def predicted(amplitudes):
    a, b, c = amplitudes
    return dict(K=4*a*a + Fraction(9, 2)*b*b + 3*c*c,
                E=4*a*a + 9*b*b + 9*c*c,
                D=4*a*a + 18*b*b + 27*c*c,
                S=a*b*c)


if __name__ == '__main__':
    controls = ((1, 1, 1), (1, 2, -3), (1, 1, 0),
                (0, 1, 1), (1, 0, 1), (-1, 1, 1))
    for case in controls:
        observed = evaluate(case)
        expected = predicted(case)
        assert observed == expected, (case, observed, expected)
        print(case, observed, 'PASS')
    print('NS-REIK-006: 6/6 exact quadrature controls PASS')
