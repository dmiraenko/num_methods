import sys, os
sys.path.append(os.path.abspath('../../../'))

from nm_pack import linalg as la

# Solution for first task
# Execute program with `solution.py <file path>`. Example: `solution.py data/LS1.DAT`
# Outputs solution for linear equation defined in the AVA format, with six digits after comma.
if(__name__ == "__main__"):
    filename = sys.argv[1]
    with open(filename, "r") as finp:
        n = int(finp.readline().strip())
        m = [None for _ in range(n)]
        v = [None for _ in range(n)]
        for i in range(n):
            vals = [float(s) for s in finp.readline().strip().split(" ") if len(s) != 0]
            m[i] = vals[0:-1]
            v[i] = vals[-1]

    print(la.Matrix(m).linsolve(la.Vector(v)))

