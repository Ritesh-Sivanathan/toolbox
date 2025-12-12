# from toolbox.mathematics.linear_algebra.matrices import Matrix
# from toolbox.mathematics.linear_algebra.MatOPS import MatOPS
# import sympy as sp

# M = [[2, 0, 1, 3], [1, -1, 2, 4], [3, 2, 0, 1], [5, 1, 3, 2]]
# A = Matrix(man=M)
# print(A.inverse().matrix)
# print(MatOPS.inverse(A))
# print(sp.Matrix(M).inverse_ADJ())

from mathematics.core.base import Constant, Expression
from mathematics.core.operators import Add, Multiply

a = 5 - Constant(3) 
print(a)

# a = Constant(2) - Constant(1) + 2
# b = Constant(4) / Constant(2) * 3
# c = 3 / Constant(3)
# d = 4 - Constant(3) * 2

# e = Expression(Add(Add(2, 3), Add(3,5)))

# print(a.value, b.value, c.value, d.value)
# print(e)
# print(e.evaluate())
