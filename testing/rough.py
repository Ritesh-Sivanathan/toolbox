from ..mathematics.linear_algebra.matrices import Matrix

A = Matrix(2,2, mode="fill",fill=5)
print(A.matrix)
print(A.show())
print(A.det())
print(repr(A))