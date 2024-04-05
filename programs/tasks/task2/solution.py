import sys, os
sys.path.append(os.path.abspath('../../../'))

# from nm_pack import linalg as la
import sympy
from nm_pack import nleq


if __name__ == "__main__":
    a0, b0, c0, x, P, K, T = sympy.symbols('a0 b0 c0 x P K T')

    a = nleq.Function('a0-x')
    b = nleq.Function('b0-3*x')
    c = nleq.Function('c0+2*x')

    ammonia_eq = nleq.Function('K * P**2 * (a0-x) * (b0-3*x)**3 - ((c0+2*x)*(a0+b0+c0-2*x))**2')

    k_eq = nleq.Function('exp(28.42282 + 9015.631 / T - 8.221117 * ln(T) + 5.00294*10**(-3) * T - 5.14102 * 10**(-7) * T**2)')


    conditions = [
        {a0: 1, b0: 3, c0: 0, P: 100, T: 400, K: 0},
        {a0: 1, b0: 3, c0: 0, P: 100, T: 500, K: 0},
        {a0: 1, b0: 3, c0: 0, P: 100, T: 600, K: 0},
        {a0: 1, b0: 3, c0: 0, P: 100, T: 700, K: 0},
        {a0: 1, b0: 3, c0: 0, P: 100, T: 800, K: 0},

        {a0: 1, b0: 3, c0: 0, P: 1,    T: 500, K: 0},
        {a0: 1, b0: 3, c0: 0, P: 10,   T: 500, K: 0},
        {a0: 1, b0: 3, c0: 0, P: 100,  T: 500, K: 0},
        {a0: 1, b0: 3, c0: 0, P: 1000, T: 500, K: 0},
    ]



    for cc in conditions:

        vals = cc.copy()

        vals.update({K: float(k_eq(vals))})
        curr_eq = nleq.Function(ammonia_eq(vals))
        soln = curr_eq.nlsolve_bisect(-vals[c0] / 2, min(vals[a0], vals[b0] / 3))
        vals.update({x: soln})

        print(f"{soln:.6f} {a(vals):.6f} {b(vals):.6f} {c(vals):.6f}")
