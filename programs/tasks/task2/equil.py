import sys, os
sys.path.append(os.path.abspath('../../../'))

# from nm_pack import linalg as la
import sympy
from nm_pack import nleq
from ast import literal_eval
from math import exp


if __name__ == "__main__":
    num = int(input("Provide number of system: "))

    # Read system
    with open("systems.txt", "r") as finp:
        for line in finp:
            if(f"{num}." in line[:3]): break
        if not line: raise ValueError("No system with such number.")
        eqn_str = line[3:].strip()
        coefs = literal_eval(finp.readline().strip())
        species = literal_eval(finp.readline())
        lnKp_eqn = sympy.parse_expr(finp.readline())
        t_range = [s for s in finp.readline().strip().split() if len(s) != 0]
        t_range = [float(t_range[2]), float(t_range[4])]

        params = dict()
        while(True):
            line = [s for s in finp.readline().strip().split() if len(s) != 0]
            if(line[1] != "="): break
            params.update({sympy.symbols(line[0]) : float(line[2])})

    print("Chose equation: " + eqn_str)

    T, P, K, x = sympy.symbols("T P K x")
    Tval = float(input("Provide temperature: "))
    if(Tval < t_range[0] or t_range[1] < Tval): raise Exception("Given temperature outside expected range.")
    Pval = float(input("Provide pressure: "))

    params.update({T: Tval, P: Pval})
    params.update({K: exp(float(lnKp_eqn.subs(params)))})

    sum_coefs = 0
    sum_eqn = sympy.parse_expr("0")
    eqns = [[], []]
    print("Provide initial concentrations for:")

    # Prepare reactant part
    react_eqn = sympy.parse_expr("K")
    react_min = float("inf")
    for i in range(len(coefs[0])):
        r = sympy.symbols(f"r{i}")
        v = float(input(species[0][i] + ": "))
        params.update({r:v})
        eqns[0].append(sympy.parse_expr(f"(r{i} - {coefs[0][i]} * x)"))
        sum_eqn += eqns[0][i]
        sum_coefs += coefs[0][i]
        react_eqn *= eqns[0][i]**coefs[0][i]
        react_min = min(react_min, v / coefs[0][i])

    # Prepare product part
    prod_eqn = sympy.parse_expr("1")
    prod_max = float("-inf")
    for i in range(len(coefs[1])):
        r = sympy.symbols(f"p{i}")
        v = float(input(species[1][i] + ": "))
        params.update({r:v})
        eqns[1].append(sympy.parse_expr(f"(p{i} + {coefs[1][i]} * x)"))
        sum_eqn += eqns[1][i]
        sum_coefs -= coefs[1][i]
        prod_eqn *= eqns[1][i]**coefs[1][i]
        prod_max = max(prod_max, -v / coefs[1][i])

    if(sum_coefs > 0):
        react_eqn *= P**sum_coefs
        prod_eqn *= sum_eqn**sum_coefs
    elif(sum_coefs < 0):
        prod_eqn *= P**(-sum_coefs)
        react_eqn *= sum_eqn**(-sum_coefs)
    final_eqn = nleq.Function((react_eqn - prod_eqn).subs(params))
    print(final_eqn.fn)

    soln = final_eqn.nlsolve_bisect(prod_max, react_min)
    params.update({x:soln})

    print("Results:")
    for i in range(len(coefs[0])): print(f"{species[0][i]}: {float(eqns[0][i].subs(params)):.6f}")
    for i in range(len(coefs[1])): print(f"{species[1][i]}: {float(eqns[1][i].subs(params)):.6f}")