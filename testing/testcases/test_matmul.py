from toolbox.mathematics.linear_algebra.matrices import Matrix
from toolbox.mathematics.linear_algebra.MatOPS import MatOPS

import unittest
import sympy

class MatMulTests(unittest.TestCase):

    def test_identity_2x2(self):

        A = Matrix(man=[[1,0],[0,1]])
        B = sympy.Matrix([[1,0],[0,1]])*2

        X = MatOPS.matmul(A,2)
        B = B.tolist()

        self.assertEqual((A*2).matrix,X,B)

if __name__ == "__main__":
    unittest.main()