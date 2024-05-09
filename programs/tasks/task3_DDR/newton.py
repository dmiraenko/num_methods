import sys, os
sys.path.append(os.path.abspath('../../../'))

# from nm_pack import linalg as la
import sympy
from nm_pack import nleq

if __name__ == "__main__":
    num = int(input("Provide number of system: "))

    with open("systems.txt", "r") as finp:
        for line in finp:
            if(f"{num}." in line[:3]): break

        if(not line): raise ValueError("No system with such number.")

        nsys = int(line.strip().split()[-1])
        funcs = []
        for i in range(nsys):
            s = [sympy.parse_expr(l.strip()) for l in finp.readline().split("=")]
            funcs.append(nleq.Function(s[0] - s[1]))

    nlsys = nleq.NLsys(funcs)
    print("Provide initial approximations:")
    init_cond = dict()
    for i in range(nlsys.nvar): init_cond.update({nlsys.vars[i] : float(input(f"{nlsys.vars[i]}: ".rjust(5)))})

    ans = nlsys.solve_newton(init_cond, True)


