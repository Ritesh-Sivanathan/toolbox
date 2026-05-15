import unittest
import numpy as np

from mathematics.linear_algebra.matrices import Matrix
from mathematics.linear_algebra.MatOPS import MatOPS

class TestDeterminant(unittest.TestCase):

    # Test on identity matrices (and non-Matrix objects as well)
    
    def test_identity_2x2(self):

        M = [[1,0],[0,1]]
        A = Matrix(man=M)

        self.assertEqual(A.det(), MatOPS.det(M), 1)
    
    def test_identity_3x3(self):

        M =[[1,0,0], [0,1,0], [0,0,1]]
        A = Matrix(man=M)

        self.assertEqual(A.det(), MatOPS.det(A), 1)

    def test_idenity_4x4(self):

        M = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        A = Matrix(man=M)

        self.assertEqual(A.det(), MatOPS.det(M), 1)

    # Test on random matrices (and Matrix objects)

    def test_matrix_random(self):

        A = Matrix(3,3, mode="rand")

        self.assertEqual(A.det(), MatOPS.det(A))
        self.assertAlmostEqual(MatOPS.det(A), np.linalg.det(A.matrix), places=5) # using AlmostEqual because np has FP precision

    # Test on manually set matrices

    def test_matrix_man_3x3(self):

        A = Matrix(man=[[2,4,3],[1,-1,6],[4,8,3]])
        self.assertEqual(A.det(), MatOPS.det(A), 18)

    def test_matrix_man_3x3_2(self):

        A = Matrix(man=[[2,4,6],[1,2,3],[0,0,0]])
        self.assertEqual(A.det(), MatOPS.det(A), 0)
    
    def test_matrix_man_3x3_3(self):

        A = Matrix(man=[[3,0,2],[2,0,-2],[0,1,1]])
        self.assertEqual(A.det(), MatOPS.det(A), 10)

if __name__ == "__main__":
    unittest.main()