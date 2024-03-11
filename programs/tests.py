# Tests for routines defined in directory `nm_pack`
import sys, os
sys.path.append(os.path.abspath('../'))

from nm_pack import nm_utils as nm
from nm_pack import linalg as la
import numpy as np

TOL = 1000 * sys.float_info.epsilon
N = 6

# Determinant test
np_mat = np.random.random((N,N))
np_det = np.linalg.det(np_mat)
la_mat = la.Matrix(np.matrix.tolist(np_mat))
la_det = la_mat.det()
if(abs(la_det - np_det) > TOL):
    raise Exception(f"Incorrect determinant.\nExpected: {np_det}\nGot: {la_det}")

# Linear equation test
np_vec = np.random.random((N,))
np_soln = np.linalg.solve(np_mat, np_vec)
la_vec = la.Vector(np.matrix.tolist(np_vec))
la_soln_triv = la_mat.linsolve(la_vec, solver="gauss_trivial")
la_soln_cram = la_mat.linsolve(la_vec, solver="cramer")
la_soln = la_mat.linsolve(la_vec)
if(any([abs(np_soln[i] - la_soln[i]) > TOL for i in range(N)])):
    raise Exception(f"Incorrect linear equation solution.\nExpected: {np_soln}\nGot: {la_soln}")

# Inverstion test
np_inv = np.linalg.inv(np_mat)
la_inv = la_mat.inverse()
if(any([any([abs(np_inv[i][j] - la_inv[i][j]) > TOL for j in range(N)]) for i in range(N)])):
    raise Exception(f"Incorrect inverse matrix.\nExpected: {np_inv}\nGot: {la_inv}")