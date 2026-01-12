# from toolbox.mathematics.linear_algebra.matrices import Matrix
# from toolbox.mathematics.linear_algebra.MatOPS import MatOPS
# import sympy as sp

# M = [[2, 0, 1, 3], [1, -1, 2, 4], [3, 2, 0, 1], [5, 1, 3, 2]]
# A = Matrix(man=M)
# print(A.inverse().matrix)
# print(MatOPS.inverse(A))
# print(sp.Matrix(M).inverse_ADJ())

from mathematics.core.base import Constant

x = Constant(1)
y = Constant(2)

expr = (Constant(1) + Constant(2)) + Constant(3) - Constant(6)

print(expr.evaluate())