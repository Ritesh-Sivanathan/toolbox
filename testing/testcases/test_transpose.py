import unittest
import numpy as np

from toolbox.mathematics.linear_algebra.matrices import Matrix
from toolbox.mathematics.linear_algebra.MatOPS import MatOPS

class TestTranspose(unittest.TestCase):

    """
    
    Testing the `MatOPS.T()`(transpose) function

    """

    def test_identity_2x2(self):

        A = [[1,0],[0,1]]
        B = [[1,0],[0,1]]

        self.assertEqual(Matrix(man=A).T().matrix, MatOPS.T(A),B)
    
    def test_random_3x3(self):

        A = Matrix(3,3,mode="rand")
        B = np.transpose(A.matrix)

        self.assertTrue(np.array_equal(MatOPS.T(A), B, A.T().matrix))
    
    def test_random_4x4(self):

        A = Matrix(4,4,mode="rand")
        B = np.transpose(A.matrix)

        self.assertTrue(np.array_equal(MatOPS.T(A),B, A.T().matrix))

if __name__ == "__main__":
    unittest.main()