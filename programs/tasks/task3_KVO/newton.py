import math
from math import exp, log, sin, cos, pi
import sys


def print_variants():
    print("Var 1:\n", "xln(x) + yln(y) = 1\n", "x^(1/3) + y^(1/3) = 2\n")
    print("Var 2:\n", "xln(x) + yln(y) = 1\n", "(x + ln(x)) * (y + ln(y)) = 1\n")
    print("Var 3:\n", "x^2 + y^2 = 1\n", "exp(-x^2) * exp(-2y^2) = 0.25\n")
    print("Var 4:\n", "(x + ln(x)) * (y + ln(y)) = 1\n", "y^3 - x^3 = 0.1\n")
    print("Var 5:\n", "x^3 + y^3 = 1\n", "exp(-x^2) + exp(-y^2) = 1.25\n")
    print("Var 6:\n", "(x^2 + 1) * (y^2 - 1) = 1\n", "(x + ln(x)) * (y + ln(y)) = 1\n")
    print("Var 7:\n", "exp(x) = ln(y)\n", "exp(-x) = ln(y-1)\n")
    print("Var 8:\n", "x^2 + y^2 = 1\n", "x^3 + y^3 = 0.9\n")
    print("Var 9:\n", "x^3 - y^3 = 0.5\n", "sin(x^2) + cos(y^2) = 1\n")
    print("Var 10:\n", "x^3 - y^3 = 1\n", "x*exp(-x^2) - y*exp(-y^2) = 0.5\n")
    print("Var 11:\n", "2x^2 - xy - 5x + 1 = 0\n", "x + 3lg(x) - y^2 = 0\n")
    print("Var 12:\n", "2x^3 - y^2 = 1\n", "(x*y^2 - 1)y = 4\n")
    print(
        "Var 13:\n",
        "x^2 + y^2 + z^2 = 1\n",
        "2x^2 + y^2 - 4z = 0\n",
        "3x^2 - 4y + z^2 = 0\n",
    )
    print("Var 14:\n", "x^2 + y^2 = 1\n", "0.5x^3 + 3x*y^2 = 1\n")
    print(
        "Var 15:\n",
        "x + x^2 - 2yz = 0.1\n",
        "y - y^2 + 3xz = -0.2\n",
        "z + z^2 + 2xy = 0.3\n",
    )
    print("Var 16:\n", "x^2 - y^2 = 1\n", "(x^2 + y^2)*sqrt(x-y) = 2\n")
    print("Var 17:\n", "5x - 6y + 20lg(x) + 16 = 0\n", "2x + y - 10lg(y) - 4 = 0\n")
    print("Var 18:\n", "x - y - lg(x) = 1\n", "x - 3y - 6lg(y) = 2\n")
    print("Var 19:\n", "2x^2 + y^2 = 1\n", "x^3 + 6y*x^2 = 1\n")
    print(
        "Var 20:\n",
        "3x^2 + 1.5y^2 + z^2 = 5\n",
        "6xyz - x + 5y + 3z = 0\n",
        "(5x - y)z = 1\n",
    )
    print("Var 21:\n", "(x^2 + y^2 - x)^2 = 2(x^2 + y^2)\n", "x^3 - 4xy + y^3 = 0\n")
    print(
        "Var 22:\n",
        "sin(4*pi*x) * sin(2*pi*y) - sin(2*pi*x) * sin(4*pi*y) = -0.75\n",
        "cos(8*pi*x) + cos(8*pi*y) = 0.25\n",
    )
    print("Var 23:\n", "x^5 + y^5 = 0.25\n", "y^3 - x^3 = 0.25\n")
    print(
        "Var 24:\n", "exp(-5x^2) + exp(-5y^2) = 0.75\n", "exp(-x^2) + exp(-y^2) = 1.5\n"
    )
    print(
        "Var 25:\n", "exp(-x^2) + exp(-y^2) = 1.25\n", "exp(-x^2) * exp(-2y^2) = 0.2\n"
    )


num_of_eq = (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2)


F = {
    1: lambda r: [
        (-1.0) * (r[0] * log(r[0]) + r[1] * log(r[1]) - 1),
        (-1.0) * (r[0] ** (1 / 3) + r[1] ** (1 / 3) - 2),
    ],
    2: lambda r: [
        (-1.0) * (r[0] * log(r[0]) + r[1] * log(r[1]) - 1),
        (-1.0) * ((r[0] + log(r[0])) * (r[1] + log(r[1])) - 1),
    ],
    3: lambda r: [
        -(r[0] ** 2 + r[1] ** 2 - 1),
        -(exp(-(r[0] ** 2)) * exp(-2 * r[1] ** 2) - 0.25),
    ],
    4: lambda r: [
        -((r[0] + log(r[0])) * (r[1] + log(r[1])) - 1),
        -(r[1] ** 3 - r[0] ** 3 - 0.1),
    ],
    5: lambda r: [
        -(r[0] ** 3 + r[1] ** 3 - 1),
        -(exp(-(r[0] ** 2)) + exp(-(r[1] ** 2)) - 1.25),
    ],
    6: lambda r: [
        -((r[0] ** 2 + 1) * (r[1] ** 2 - 1) - 1),
        -((r[0] + log(r[0])) * (r[1] + log(r[1])) - 1),
    ],
    7: lambda r: [-(exp(r[0]) - log(r[1])), -(exp(-r[0]) - log(r[1] - 1))],
    8: lambda r: [-(r[0] ** 2 + r[1] ** 2 - 1), -(r[0] ** 3 + r[1] ** 3 - 0.9)],
    9: lambda r: [
        -(r[0] ** 3 - r[1] ** 3 - 0.5),
        -(sin(r[0] ** 2) + cos(r[1] ** 2) - 1),
    ],
    10: lambda r: [
        -(r[0] ** 3 - r[1] ** 3 - 1),
        -(r[0] * exp(-(r[0] ** 2)) - r[1] * exp(-(r[1] ** 2)) - 0.5),
    ],
    11: lambda r: [
        -(2 * r[0] ** 2 - r[0] * r[1] - 5 * r[0] + 1),
        -(r[0] + 3 * math.log10(r[0]) - r[1] ** 2),
    ],
    12: lambda r: [
        -(2 * r[0] ** 3 - r[1] ** 2 - 1),
        -((r[0] * r[1] ** 2 - 1) * r[1] - 4),
    ],
    13: lambda r: [
        -(r[0] ** 2 + r[1] ** 2 + r[2] ** 2 - 1),
        -(2 * r[0] ** 2 + r[1] ** 2 - 4 * r[2]),
        -(3 * r[0] ** 2 - 4 * r[1] + r[2] ** 2),
    ],
    14: lambda r: [
        -(r[0] ** 2 + r[1] ** 2 - 1),
        -(0.5 * r[0] ** 3 + 3 * r[0] * r[1] ** 2 - 1),
    ],
    15: lambda r: [
        -(r[0] + r[0] ** 2 - 2 * r[1] * r[2] - 0.1),
        -(r[1] - r[1] ** 2 + 3 * r[0] * r[2] + 0.2),
        -(r[2] + r[2] ** 2 + 2 * r[0] * r[1] - 0.3),
    ],
    16: lambda r: [
        -(r[0] ** 2 - r[1] ** 2 - 1),
        -((r[0] ** 2 + r[1] ** 2) * math.sqrt(r[0] - r[1]) - 2),
    ],
    17: lambda r: [
        -(5 * r[0] - 6 * r[1] + 20 * math.log10(r[0]) + 16),
        -(2 * r[0] + r[1] - 10 * math.log10(r[1]) - 4),
    ],
    18: lambda r: [
        -(r[0] - r[1] - 6 * math.log10(r[0]) - 1),
        -(r[0] - 3 * r[1] - 6 * math.log10(r[1]) - 2),
    ],
    19: lambda r: [
        -(2 * r[0] ** 2 + r[1] ** 2 - 1),
        -(r[0] ** 3 + 6 * r[0] ** 2 * r[1] - 1),
    ],
    20: lambda r: [
        (-1.0) * (3 * r[0] ** 2 + 1.5 * r[1] ** 2 + r[2] ** 2 - 5),
        (-1.0) * (6 * r[0] * r[1] * r[2] - r[0] + 5 * r[1] + 3 * r[2]),
        (-1.0) * ((5 * r[0] - r[1]) * r[2] - 1),
    ],
    21: lambda r: [
        -((r[0] ** 2 + r[1] ** 2 - r[0]) ** 2 - 2 * (r[0] ** 2 + r[1] ** 2)),
        -(r[0] ** 3 - 4 * r[0] * r[1] + r[1] ** 3),
    ],
    22: lambda r: [
        -(
            sin(4 * pi * r[0]) * sin(2 * pi * r[1])
            - sin(2 * pi * r[0]) * sin(4 * pi * r[1])
            + 0.75
        ),
        -(cos(8 * pi * r[0]) + cos(8 * pi * r[1]) - 0.25),
    ],
    23: lambda r: [-(r[0] ** 5 + r[1] ** 5 - 0.25), -(r[1] ** 3 - r[0] ** 3 - 0.25)],
    24: lambda r: [
        -(exp(-5 * r[0] ** 2) + exp(-5 * r[1] ** 2) - 0.75),
        -(exp(-(r[0] ** 2)) + exp(-(r[1] ** 2)) - 1.5),
    ],
    25: lambda r: [
        -(exp(-(r[0] ** 2)) + exp(-(r[1] ** 2)) - 1.25),
        -(exp(-(r[0] ** 2)) * exp(-2 * r[1] ** 2) - 0.2),
    ],
}

dF = {
    1: lambda r: [
        [log(r[0]) + 1, log(r[1]) + 1],
        [r[0] ** (-2 / 3) / 3, r[1] ** (-2 / 3) / 3],
    ],
    2: lambda r: [
        [log(r[0]) + 1, log(r[1]) + 1],
        [
            (1 + 1 / r[0]) * (r[1] + log(r[1])),
            (1 + 1 / r[1]) * (r[0] + log(r[0])),
        ],
    ],
    3: lambda r: [
        [2 * r[0], 2 * r[1]],
        [
            (-2 * r[0]) * exp(-(r[0] ** 2)) * exp(-2 * r[1] ** 2),
            -4 * r[1] * exp(-(r[0] ** 2)) * exp(-2 * r[1] ** 2),
        ],
    ],
    4: lambda r: [
        [
            (1 + 1 / r[0]) * (r[1] + log(r[1])),
            (1 + 1 / r[1]) * (r[0] + log(r[0])),
        ],
        [-3 * r[0] ** 2, 3 * r[1] ** 2],
    ],
    5: lambda r: [
        [
            3 * r[0] ** 2,
            3 * r[1] ** 2,
        ],
        [-2 * r[0] * exp(-(r[0] ** 2)), -2 * r[1] * exp(-(r[1] ** 2))],
    ],
    6: lambda r: [
        [2 * r[0] * (r[1] ** 2 - 1), 2 * r[1] * (r[0] ** 1 + 1)],
        [
            (1 + 1 / r[0]) * (r[1] + log(r[1])),
            (1 + 1 / r[1]) * (r[0] + log(r[0])),
        ],
    ],
    7: lambda r: [[exp(r[0]), -1 / r[1]], [-exp(-r[0]), -1 / (r[1] - 1)]],
    8: lambda r: [[2 * r[0], 2 * r[1]], [3 * r[0] ** 2, 3 * r[1] ** 2]],
    9: lambda r: [
        [3 * r[0] ** 2, -3 * r[1] ** 2],
        [2 * r[0] * cos(r[0] ** 2), -2 * r[1] * sin(r[1] ** 2)],
    ],
    10: lambda r: [
        [3 * r[0] ** 2, -3 * r[1] ** 2],
        [
            (1 - 2 * r[0] ** 2) * exp(-(r[0] ** 2)),
            (2 * r[1] ** 2 - 1) * exp(-(r[1] ** 2)),
        ],
    ],
    11: lambda r: [[4 * r[0] - r[1] - 5, -r[0]], [1 + 3 / (r[0] * log(10)), -2 * r[1]]],
    12: lambda r: [[6 * r[0] ** 2, -2 * r[1]], [r[1] ** 3, 3 * r[0] * (r[1]) ** 2 - 1]],
    13: lambda r: [
        [2 * r[0], 2 * r[1], 2 * r[2]],
        [4 * r[0], 2 * r[1], -4.0],
        [6 * r[0], -4.0, 2 * r[2]],
    ],
    14: lambda r: [
        [2 * r[0], 2 * r[1]],
        [1.5 * r[0] ** 2 + 3 * r[1] ** 2, 6 * r[0] * r[1]],
    ],
    15: lambda r: [
        [1 + 2 * r[0], -2 * r[2], -2 * r[1]],
        [3 * r[2], 1 - 2 * r[1], 3 * r[0]],
        [2 * r[1], 2 * r[0], 1 + 2 * r[2]],
    ],
    16: lambda r: [
        [2 * r[0], -2 * r[1]],
        [
            (r[0] * (3 * r[0] - 4 * r[1]) - r[1] ** 2) / (2 * math.sqrt(r[0] - r[1])),
            (r[0] ** 2 + r[1] * (4 * r[0] - 3 * r[1])) / (2 * math.sqrt(r[0] - r[1])),
        ],
    ],
    17: lambda r: [[5 + 20 / (r[0] * log(10)), -6], [2, 1 - 10 / (r[1] * log(10))]],
    18: lambda r: [[1 - 6 / (r[0] * log(10)), -1], [1, -3 - 6 / (r[1] * log(10))]],
    19: lambda r: [
        [4 * r[0], 2 * r[1]],
        [3 * r[0] ** 2 + 12 * r[0] * r[1], 6 * r[0] ** 2],
    ],
    20: lambda r: [
        [6 * r[0], 3 * r[1], 2 * r[2]],
        [6 * r[1] * r[2] - 1, 6 * r[0] * r[2] + 5, 6 * r[0] * r[1] + 3],
        [5 * r[2], -r[2], 5 * r[0] - r[1]],
    ],
    21: lambda r: [
        [
            4 * r[0] ** 3
            - 6 * r[0] ** 2
            - 2 * r[0]
            + 4 * r[0] * r[1] ** 2
            - 2 * r[1] ** 2,
            4 * r[1] * (r[0] ** 2 + r[1] ** 2 - r[0] - 1),
        ],
        [3 * r[0] ** 2 - 4 * r[1], 3 * r[1] ** 2 - 4 * r[0]],
    ],
    22: lambda r: [
        [
            4
            * pi
            * sin(2 * pi * r[1])
            * (cos(4 * pi * r[0]) - cos(2 * pi * r[0]) * cos(2 * pi * r[1])),
            4
            * pi
            * sin(2 * pi * r[0])
            * (cos(2 * pi * r[0]) * cos(2 * pi * r[1]) - cos(4 * pi * r[1])),
        ],
        [-8 * pi * sin(8 * pi * r[0]), -8 * pi * sin(8 * pi * r[1])],
    ],
    23: lambda r: [[5 * r[0] ** 4, 5 * r[1] ** 4], [-3 * r[0] ** 2, 3 * r[1] ** 2]],
    24: lambda r: [
        [-10 * r[0] * exp(-5 * r[0] ** 2), -10 * r[1] * exp(-5 * r[1] ** 2)],
        [-2 * r[0] * exp(-(r[0] ** 2)), -2 * r[1] * exp(-(r[1] ** 2))],
    ],
    25: lambda r: [
        [-2 * r[0] * exp(-(r[0] ** 2)), -2 * r[1] * exp(-(r[1] ** 2))],
        [
            -2 * r[0] * exp(-(r[0] ** 2)) * exp(-2 * r[1] ** 2),
            -4 * r[1] * exp(-(r[0] ** 2)) * exp(-2 * r[1] ** 2),
        ],
    ],
}


def print_approx(X):
    for i in range(len(X)):
        if math.copysign(1, X[i]) < 0:
            print("  x", i, " = -", "%.15e" % abs(X[i]), sep="")
        else:
            print("  x", i, " =  ", "%.15e" % abs(X[i]), sep="")


def linsys(A, B, X, n):

    for k in range(n - 1):
        i_max = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[i_max][k]):
                i_max = i
        A.insert(k, A.pop(i_max))
        B.insert(k, B.pop(i_max))
        if A[k][k] == 0.0:
            return 1

        for i in range(k + 1, n):
            c = -A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] = A[i][j] + c * A[k][j]
            B[i] = B[i] + c * B[k]
            A[i][k] = 0.0

    if A[n - 1][n - 1] == 0.0:
        return 1

    X[n - 1] = B[n - 1] / A[n - 1][n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for i in range(k + 1, n):
            s += A[k][i] * X[i]
        X[k] = (B[k] - s) / A[k][k]
        k -= 1
    return 0


def newton(X, n, var):
    while 1:
        dX = [0.0] * n
        try:
            #            print(dF[var](X), "\n", F[var](X))
            if linsys(dF[var](X), F[var](X), dX, n):
                raise ValueError
        except ValueError:
            print("Singular matrix encountered")
            return 1
        except ZeroDivisionError:
            print("Division by zero encountered")
            return 1
        for i in range(len(X)):
            X[i] += dX[i]
        S = 0.0
        for i in dX:
            S += i**2
        if math.sqrt(S) <= 3.0 * sys.float_info.epsilon:
            print_approx(X)
            return 0
        print_approx(X)
        print("Error = ", "%.15e" % math.sqrt(S), "\nContinue? (y/n): ", sep="", end="")
        if input() == "n":
            return 1


try:
    print_variants()
    print("Variant: ", end="")
    var = int(input())
    if var < 1 or var > 25:
        raise ValueError
except ValueError:
    print("Incorrect variant! Quit")
    input()
    sys.exit(0)

try:
    print("Approximation: ", end="")
    x = list(map(float, input().split()))
    if len(x) != num_of_eq[var - 1]:
        raise ValueError
except ValueError:
    print("Incorrect input! Quit")
    input()
    sys.exit(0)

if newton(x, num_of_eq[var - 1], var):
    print("Failed to find a solution! Quit")
    input()
    sys.exit(0)
else:
    print("Converged!")
    input()

# print(F[3]([7.010865256743565e-01, -7.130762115775985e-01]))
