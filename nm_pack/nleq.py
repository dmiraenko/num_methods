import sympy as sp
from math import copysign
from . import nm_utils as nm
from . import linalg as la

TOL = nm.TOL
MAX_ITER = 1000

class Function:

    def __init__(self, val, order = None):
        if(type(val) == str):
            self.fn = sp.parse_expr(val)
        else:
            self.fn = val
        self.free_symbols = self.fn.free_symbols
        # fs = self.fn.free_symbols
        # if(order == None):
        #     self.args = list(fs)
        # else:
        #     self.args = [y for _, y in sorted([(order.index(str(f)), f) for f in fs], key = lambda x: x[0])]

        # self.args = sorted(list(self.fn.free_symbols), key = lambda x: int(str(x)[1:]))
        # for i in range(len(self.args)):
        #     if(str(self.args[i])[0] != 'x' or int(str(self.args[i])[1:]) != i+1):
        #         raise Exception("All function symbols must be named x<n> in increasing order")
        # print(self.args)

    def __call__(self, vars_vals):
        if(type(vars_vals) == float):
            return self.fn.subs({f : vars_vals for f in self.fn.free_symbols})
        else:
            return self.fn.subs(vars_vals)

    def __str__(self):
        return self.fn.__str__()

    # def expand_args(self, args):
    #     if(type(args[0]) == str):
    #         self.args = list(sp.symbols(" ".join(args)))
    #     else:
    #         self.args = args

    def diff(self, args = None):
        if(args == None):
            return [Function(self.fn.diff(a)) for a in self.free_symbols]
        else:
            return [Function(self.fn.diff(a)) for a in args]

    def nlsolve_bisect(self, a, b):
        if(len(self.fn.free_symbols) != 1): raise Exception("Cannot use bisection to solve multivariate equations.")
        va = self(a)
        vb = self(b)
        if(abs(va) < TOL): return a
        if(abs(vb) < TOL): return b
        if(copysign(1.0, va) * copysign(1.0, vb) >= 0): raise Exception("Bisection method requires given function to have different signs an endpoints.")

        # Make sure a < b
        if(a < b): a1, b1 = a, b
        else: a1, b1, va, vb = b, a, vb, va

        for iter in range(MAX_ITER):
            # Find midpoint and its value
            c = a1 + (b1-a1)/2
            vc = self(c)

            # Leave if hit exact zero
            if(vc == 0): return c

            # Update endpoints so that new endpoint signs still have different signs
            if(copysign(1.0, va) * copysign(1.0, vc) < 0): b1, vb = c, vc
            else: a1, va = c, vc

            # Leave if endpoints are close enough
            if(b1 - a1 < TOL): return c

        # Exception if exceeded iteration limit
        if(iter >= MAX_ITER): raise Exception("Exceeded iteration limit")

    def solve_simple_iter(self, iter_fn, x0 : list):
        pass

    def nlsolve_newton(self, x0 : float):
        if(len(self.fn.free_symbols) != 1): raise Exception("Cannot single-variable Newton to solve multivariate equations.")
        d = self.diff()[0]
        x = x0
        for iter in range(MAX_ITER):
            dx = float(self(x) / d(x))
            x -= dx
            if(abs(dx) < TOL): return x

        if(iter >= MAX_ITER): raise Exception("Exceeded iteration limit")

class NLsys:

    def __init__(self, funcs):
        self.neq = len(funcs)
        vars = set()
        for f in funcs: vars |= f.free_symbols
        self.nvar = len(vars)

        # Move to solver
        if(self.neq > self.nvar): raise Exception("System is overdefined. Cannot provide solution.")
        if(self.neq < self.nvar): raise Exception("System is underdefined. Cannot provide a point-like solution.")

        self.vars = sorted(list(vars), key = str)
        self.funcs = funcs

    def jacobian(self):
        return [f.diff(self.vars) for f in self.funcs]

    def jacobian_val(self, vars_vals):
        return [[fd(vars_vals) for fd in f.diff(self.vars)] for f in self.funcs]

    def solve_newton(self, init_cond, verbose = False):
        if(set(self.vars) != set(init_cond)): raise Exception("Initial conditions' variable list does not match NL system's argument list.")
        jac = self.jacobian()
        x = init_cond.copy()

        # Allocate vector and jacobian
        vals = la.Vector([0.0] * self.nvar)
        jacv = la.Matrix([[0.0] * self.nvar for _ in range(self.nvar)])

        for iter in range(MAX_ITER):
            # Set vector and jacobian
            for i in range(self.nvar):
                vals[i] = self.funcs[i](x)
                for j in range(self.nvar): jacv[i][j] = jac[i][j](x)

            dx = jacv.linsolve(vals)

            for i in range(self.nvar): x[self.vars[i]] -= dx[i]

            lx = dx.len()

            if(verbose):
                for xx in x: print(f"{xx}: ".rjust(5) + f"{x[xx]:.16e}".rjust(28))
                print("dX norm: " + f"{lx:.16e}".rjust(22))

            if(lx < TOL): return x
