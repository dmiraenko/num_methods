from math import sqrt, exp, cos, sin, asin, log
import numpy as np

p = 3.14159265358979323846264
p2 = p / 2

def simpson_int(f, a, b, eps = 1e-15, check_err = False):
    n = 1
    h = (b - a) / 2
    s1 = f(a) + f(b)
    s3 = 0.0
    I = s1 * h
    I_old = float("inf")
    r = I_old
    if(check_err):
        print("      Approximation       |             Rh            |      Rh / R(h/2)")
        print("                          |                           |")

    while(r > eps):
        I_old = I
        r_old = r
        s2 = 0.0
        for k in range(n):
            s2 += f(a + (2*k+1)*h)
        I = h * (s1 + 4 * s2 + 2 * s3) / 3
        s3 += s2
        n *= 2
        h /= 2
        r = abs(I - I_old)
        if(check_err):
            print(f"{I:.16e}".rjust(20), "   |", f"{r:.16e}".rjust(20), "   |", f"{np.float64(r_old) / np.float64(r):.16f}".rjust(20))

    return I, n // 2, h * 2

def var1():

    print("Data for I1")
    _, n1, _ = simpson_int(sqrt, 0.0, 1.0, 1e-9, True)
    print(f"Number of sub-intervals = {n1}\n")
    print("Data for I2")
    _, n2, _ = simpson_int(sqrt, 1.0, 2.0, 1e-9, True)
    print(f"Number of sub-intervals = {n2}\n")

def var2():

    def ff(x): return exp(-x**2)

    true_val = 1.772453850905516027298

    a = 0.0
    I = 0.0
    while(abs(true_val - 2 * I) > 1e-15): # сказать студентам!
        I, _, _ = simpson_int(ff, 0.0, a, 1e-12)
        a += 0.25
    print(f"Best value (0.25 error) = {a:.2f}")

def var3():

    n = 5
    def ff(x): return x**n * exp(x-1.0)

    def ebad():
        e = 0.3678794411714423
        for i in range(2, n+1):
            e = 1 - i * e
        return e

    def egood():
        e = 1/25
        for i in range(24, n, -1):
            e = (1 - e) / i
        return e


    for n in range(5, 20, 5):
        I, _, _ = simpson_int(ff, 0.0, 1.0)
        print(f"n = {n}")
        print(f"Simpson result = {I:.16f}")
        print(f"Bad recursive  = {ebad():.16f}")
        print(f"Good recursive = {egood():.16f}")

def var4():

    def ff(x): return 4.0 / (1.0 + x**2)

    true_val = p
    I1, _, _ = simpson_int(ff, 0, 1, 1e-3)
    I2, _, _ = simpson_int(ff, 0, 1, 1e-6)
    I3, _, _ = simpson_int(ff, 0, 1, 1e-9)
    I4, _, _ = simpson_int(ff, 0, 1, 1e-12)
    I5, _, _ = simpson_int(ff, 0, 1, 1e-15)

    print(f"True value = {true_val:.18f}")
    print(f"eps = 1e-3:  {I1:.18f}, Error = {abs(true_val - I1):.18f}")
    print(f"eps = 1e-6:  {I2:.18f}, Error = {abs(true_val - I2):.18f}")
    print(f"eps = 1e-9:  {I3:.18f}, Error = {abs(true_val - I3):.18f}")
    print(f"eps = 1e-12: {I4:.18f}, Error = {abs(true_val - I4):.18f}")
    print(f"eps = 1e-15: {I5:.18f}, Error = {abs(true_val - I5):.18f}")

def var5():

    def ff(x): return exp(-x**2)

    c = 2.0 / 1.772453850905516027298167483
    def erf(x):
        I, _, _ = simpson_int(ff, 0.0, x, 1e-14)
        return c * I

    for k in range(21):
        print(f"{k/10:.2f} {erf(k/10):.16f}")

def var6():

    def ff(x): return exp(-x) * (cos(x))**2

    true_val = 3/5

    for a in range(20, 55, 5):
        I, _, _ = simpson_int(ff, 0, a, 1e-14)
        D, _, _ = simpson_int(ff, a, 90, 1e-14)
        print(f"a = {a}\nError = {abs(I-true_val):.16f}\nTail integral = {D:.16f}")

def var7():

    def ff(x): return exp(-x) * (cos(x**2))

    true_val = 0.534877974533517566326332843

    for a in range(15, 45, 5):
        I, _, _ = simpson_int(ff, 0, a, 5e-15)
        D, _, _ = simpson_int(ff, a, 75, 5e-15)
        print(f"a = {a}\nError = {abs(I-true_val):.16f}\nTail integral = {D:.16f}")

def var8():

    def ff(x):
        if(x == 0):
            return 1.0
        else:
            return sin(x) / x

    a = 0.0
    while(a <= 16):
        I, _, _ = simpson_int(ff, 0.0, a, 1e-14)
        print(f"{a:.2f} {I:.16f}")
        a += 0.25

def var9():

    def ff(x): return sqrt(1 - x**2)

    true_val = p2

    I, _, _ = simpson_int(ff, -1.0, 1.0, 1e-10, True)

def var10():

    def ff(x): return 1.0 / (1 - x + x**2)

    true_val = 1.209199576156145233729385505

    I, _, _ = simpson_int(ff, 0.0, 1.0, 1e-14, True)

def var11():

    def ff(x): return 1.0 / (1 + 25 * x**2)

    true_val = 0.54936030677800634434450877

    I, _, _ = simpson_int(ff, -1.0, 1.0, 1e-14, True)

def var12():

    def ff(x): return sqrt(x - x**2)

    true_val = 0.3926990816987241548078304229

    I, _, _ = simpson_int(ff, 0.0, 1.0, 1e-12, True)

def var13():

    def ff(x):
        if(x == 0):
            return 1.0
        else:
            return (x / sin(x))**2

    c = p2
    true_val = 2.177586090303602130500688898

    I, _, _ = simpson_int(ff, 0.0, c, 1e-14, True)

def var14():

    x = 0.0
    n = 0
    def ff(y): return exp(x * cos(y)) * cos(n*y)

    x = 0.0
    print(" x           I0                  I1")
    while(x <= 3):
        n = 0
        I0, _, _ = simpson_int(ff, 0.0, p, 1e-14)
        I0 /= p
        n = 1
        I1, _, _ = simpson_int(ff, 0.0, p, 1e-14)
        I1 /= p
        print(f"{x:.2f} {I0:.16f} {I1:.16f}")
        x += 0.05

def var15():

    x = 0.0
    n = 0
    def ff(y): return cos(n * y - x * sin(y))

    x = 0.0
    print(" x           J0                  J1")
    while(x <= 16):
        n = 0
        I0, _, _ = simpson_int(ff, 0.0, p, 1e-14)
        I0 /= p
        n = 1
        I1, _, _ = simpson_int(ff, 0.0, p, 1e-14)
        I1 /= p
        print(f"{x:.1f} {I0:.16f} {I1:.16f}")
        x += 0.1

def var16():

    a = 0.0
    def ff(x):
        if(x == 0):
            return a / p
        else:
            return - log(1 - a * sin(x)) / (p*sin(x))

    aa = [0.25, 0.5, 0.75, 1 - 1e-6, 1 - 1e-9, 1 - 1e-12]
    epss = [1e-14, 1e-14, 1e-14, 1e-12, 1e-10, 1e-10]
    for v in aa:
        a = v
        I, _ , _ = simpson_int(ff, -p2, p2, 1e-12, True)
        print(f"Results for a = {a:.12f}")
        print(f"arcsin from integral = {I:.16f}")
        print(f"True arcsin =          {asin(a):.16f}\n")

def var17():

    def ff(x):
        if(x == 0):
            return 0
        else:
            return sin(x) * log(sin(x))

    I, _, _ = simpson_int(ff, 0, p2, 1e-14, True)

def var18():

    def ff(x): return x * log(1 + x)

    I, _, _ = simpson_int(ff, 0, 1, 1e-15, True)

def var19():

    def ff(x): return x**2*exp(-2*x)

    true_val = 0.25

    for a in range(15, 26):
        I, _, _ = simpson_int(ff, 0, a, 1e-13)
        D, _, _ = simpson_int(ff, a, 75, 1e-13)
        print(f"a = {a}\nError = {abs(I-true_val):.16f}\nTail integral = {D:.16f}")

def var20():
    pp = 1.5
    def ff(x):
        if(x == 0):
            return 0
        else:
            return x**3 / (exp(pp*x) - 1)

    true_val = (p / pp)**4 / 15

    for a in range(15, 45, 5):
        I, _, _ = simpson_int(ff, 0, a, 1e-14)
        D, _, _ = simpson_int(ff, a, 90, 1e-14)
        print(f"a = {a}\nError = {abs(I-true_val):.16f}\nTail integral = {D:.16f}")

def var21():

    def c(t): return cos(p * t ** 2 / 2)
    def s(t): return sin(p * t ** 2 / 2)

    x = 0.0
    print(" x           C                   S")
    while(x <= 4.01):
        I0, _, _ = simpson_int(c, 0.0, x, 1e-14)
        I1, _, _ = simpson_int(s, 0.0, x, 1e-14)
        print(f"{x:.2f} {I0:.16f} {I1:.16f}")
        x += 0.02

def var22():

    def dx(t):
        if(t == 0):
            return 0
        else:
            return t**3 / (exp(t) - 1)

    def d(x):
        if(x == 0):
            return 1
        else:
            I, _, _ = simpson_int(dx, 0, x, 1e-13)
            return I * 3 / x**3

    x = 0.0
    print(" x           D")
    while(x <= 15):
        print(f"{x:.1f} {d(x):.16f}")
        x += 0.1

    R = 8.314472
    theta = 658

    print("\n  t             C")
    for t in range(50, 1651, 25):
        x = t / theta
        D = d(x)
        C = 3 * R * (4 * D - 3 * x / (exp(x) - 1))

        print(f"{t}".rjust(5) + f"  {C:.16f}")




vars = [
    var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, # 1, 9 и 10 надо доделать!
    var11, var12, var13, var14, var15, var16, var17, var18, var19, var20,
    var21, var22
]

v = int(input("Input variant: "))

vars[v-1]()
