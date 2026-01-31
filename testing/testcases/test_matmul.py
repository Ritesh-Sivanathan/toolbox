from mathematics.linear_algebra.matrices import Matrix
from mathematics.linear_algebra.MatOPS import MatOPS

import unittest
import sympy

class MatMulTests(unittest.TestCase):

    def test_identity_2x2(self):

        A = Matrix(man=[[1,0],[0,1]])
        B = (sympy.Matrix([[1,0],[0,1]])*2).tolist()

        res1 = A * 2
        self.assertEqual(res1.matrix, B, msg="Right-sided multiplication failed")
        
        res2 = 2 * A
        self.assertEqual(res2.matrix, B, msg="Right-sided multiplication failed")

        X = MatOPS.MatMul(A,2)
        self.assertEqual(res1.matrix, X.matrix, msg="Operator and MatMul helper mismatch")

if __name__ == "__main__":
    unittest.main()