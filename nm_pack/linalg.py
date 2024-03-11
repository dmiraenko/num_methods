from . import nm_utils as nm
from sys import float_info as fi

TOL = 100 * fi.epsilon

class Vector:

    def __init__(self, arr):
        if(type(arr) != list):
            raise Exception("Initializer of class Vector was not given an array")

        self.vec = [float(a) for a in arr]
        self.n = len(arr)

    def __getitem__(self, ind):
        return self.vec[ind]

    def __setitem__(self, ind, value):
        self.vec[ind] = value

    def __str__(self) -> str:
        return "\n".join(["| " + f"{v:10.6f}" + " |" for v in self.vec])

    def copy(self):
        return Vector(self.vec.copy())

class Matrix:

    #
    # Python utility functions
    #
    def __init__(self, mat):

        # Check that the provided mat variable is actually a matrix
        if(type(mat) != list):
            raise Exception("Initializer of class Matrix was not given a matrix.")

        if(type(mat[0]) != list):
            raise Exception("Initializer of class Matrix was not given a matrix.")

        n = len(mat[0])
        for i in range(1, len(mat)):
            if(type(mat[i]) != list):
                raise Exception("Initializer of class Matrix was not given a matrix.")
            if(len(mat[i]) != n):
                raise Exception("Initializer of class Matrix was given a matrix with differing row lengths.")

        self.mat = [[float(val) for val in row] for row in mat] # Forcibly convert all values to float
        self.m = len(mat)
        self.n = n

    def __getitem__(self, ind):
        return self.mat[ind]

    def __str__(self) -> str:
        return "\n".join(["| " + " ".join([f"{v:10.6f}" for v in m]) + " |" for m in self.mat])

    def copy(self):
        return Matrix([row.copy() for row in self.mat])

    #
    # General matrix utilities
    #
    def transpose(self):
        return Matrix([[self.mat[j][i] for j in range(self.n)] for i in range(self.m)])

    def det(self) -> float:
        if(self.m != self.n):
            raise Exception("Cannot compute determinant for non-square matrix.")

        ans = 0.0
        psign = 1
        for p in nm.permutations(self.m):
            ans += psign * nm.prod([self[i][p[i]] for i in range(self.m)])
            psign = -psign
        return ans

    #
    # Linear equation solvers
    #
    def __linsolve_gauss_trivial(self, vec : Vector):
        tmat = self.copy()
        res = vec.copy()

        # Forward propagation
        for i in range(tmat.m):
            for j in range(i+1, tmat.m):
                c = -tmat[j][i] / tmat[i][i]
                for k in range(i, tmat.n): tmat[j][k] += c * tmat[i][k]
                res[j] += c * res[i]

        # Backward propagation
        for i in range(tmat.m - 1, -1, -1):
            v = 0.0
            for j in range(i+1, tmat.m): v += tmat[i][j] * res[j]
            res[i] = (res[i] - v) / tmat[i][i]

        return res


    def __linsolve_gauss(self, vec : Vector):
        tmat = self.copy()
        res = vec.copy()
        idx = [_ for _ in range(self.m)]

        # Forward propagation
        for i in range(tmat.m):
            # Find leading element
            mx_ind = i
            for j in range(i+1, tmat.m):
                if(abs(tmat[idx[j]][i]) > abs(tmat[idx[i]][i])): mx_ind = j
            idx[i], idx[mx_ind] = idx[mx_ind], idx[i]

            for j in range(i+1, tmat.m):
                c = -tmat[idx[j]][i] / tmat[idx[i]][i]
                for k in range(i, tmat.n): tmat[idx[j]][k] += c * tmat[idx[i]][k]
                res[idx[j]] += c * res[idx[i]]

        # Backward propagation
        for i in range(tmat.m - 1, -1, -1):
            v = 0.0
            for j in range(i+1, tmat.m): v += tmat[idx[i]][j] * res[idx[j]]
            res[idx[i]] = (res[idx[i]] - v) / tmat[idx[i]][i]

        # Unscramble and return
        return Vector([res[i] for i in idx])

    def __linsolve_cramer(self, vec : Vector):
        d = self.det()
        ans = vec.copy()
        tmat = self.copy()

        for j in range(self.n):
            for i in range(self.m): tmat[i][j] = vec[i]
            ans[j] = tmat.det() / d
            for i in range(self.m): tmat[i][j] = self[i][j]

        return ans

    def linsolve(self, vec : Vector, solver = "gauss"):
        if(self.m != self.n):
            raise Exception("Cannot solve linear equation. Matrix is not square.")

        if(self.m != vec.n):
            raise Exception("Cannot solve linear equation. Matrix and Vector dimensions do not match.")

        if(abs(self.det()) < TOL):
            raise Exception("Cannot solve linear equation. Matrix determinant is too close to zero.")

        if(solver == "gauss"):
            return self.__linsolve_gauss(vec)
        elif(solver == "gauss_trivial"):
            return self.__linsolve_gauss_trivial(vec)
        elif(solver == "cramer"):
            return self.__linsolve_cramer(vec)
        else:
            raise Exception("Given solver keyword, " + solver + ", does not correspond to any solver.")

    def inverse(self):
        if(self.m != self.n):
            raise Exception("Cannot invert a non-square matrix.")

        if(abs(self.det()) < TOL):
            raise Exception("Cannot invert matrix with zero determinant.")

        res = self.copy()
        evec = Vector([0 for _ in range(self.n)])

        for i in range(self.n):
            evec[i] = 1.0
            inv_col = self.__linsolve_gauss(evec)
            for j in range(self.n): res[j][i] = inv_col[j]
            evec[i] = 0.0

        return res