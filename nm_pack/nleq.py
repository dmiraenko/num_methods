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
            return [Function(self.fn.diff(a)) for a in args.keys()]

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
        args = {}
        for f in funcs: args |= f.free_symbols
        self.nvar = len(args)

        # Move to solver
        if(self.neq > self.nvar): raise Exception("System is overdefined. Cannot provide solution.")
        if(self.neq < self.nvar): raise Exception("System is underdefined. Cannot provide a point-like solution.")

        self.args = args
        self.funcs = funcs

    def jacobian(self):
        return [f.diff(self.args) for f in self.funcs]

    def jacobian_val(self, vars_vals):
        return [[fd(vars_vals) for fd in f.diff()] for f in self.funcs]

    def solve_newton(self, init_cond):
        jac = self.jacobian_val(init_cond)
        args = init_cond.copy()

        for iter in range(MAX_ITER):
            vals = la.Vector([f(init_cond) for f in self.funcs])
            jacv = la.Matrix([[ff(args) for ff in f] for f in jac])

            add = jacv.linsolve(vals)

            i = 0
            for a in args:
                a += add[i]
                i += 1

            if(add.len() < TOL): return args

if __name__ == "__main__":
    a = Function('2 * x1 + x2 ** x1', order = ['x1', 'x2'])
    print(a)
    print(a(1, 2))
    b = Function('2 * x1 + x2 ** x3', order = ['x1', 'x2', 'x3'])
    print(b)
    print(b(1, 2, 3))
    # c = Function('2 * x1 + x3 ** x1')
    # print(c)
    # d = Function('2 * x1 + y ** x1')
    # print(d)


