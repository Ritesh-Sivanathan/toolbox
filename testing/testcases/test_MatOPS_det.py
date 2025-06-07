import unittest
import numpy as np

from toolbox.mathematics.linear_algebra.matrices import Matrix, MatOPS

class TestDeterminant(unittest.TestCase):

    # Test on identity matrices (and non-Matrix objects as well)
    
    def test_identity_2x2(self):
        self.assertEqual(MatOPS.det([[1,0],[0,1]]), 1)
    
    def test_identity_3x3(self):
        self.assertEqual(MatOPS.det([[1,0,0], [0,1,0], [0,0,1]]), 1)

    def test_idenity_4x4(self):
        self.assertEqual(MatOPS.det([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]), 1)

    # Test on random matrices (and Matrix objects)

    def test_matrix_random(self):

        A = Matrix(3,3, mode="rand")

        self.assertAlmostEqual(MatOPS.det(A), np.linalg.det(A.matrix), places=5) # using AlmostEqual because np has FP precision

    # Test on manually set matrices

    def test_matrix_man_3x3(self):

        A = Matrix(man=[[2,4,3],[1,-1,6],[4,8,3]])
        self.assertEqual(MatOPS.det(A), 18)

    def test_matrix_man_3x3_2(self):

        A = Matrix(man=[[2,4,6],[1,2,3],[0,0,0]])
        self.assertEqual(MatOPS.det(A), 0)
    
    def test_matrix_man_3x3_3(self):

        A = Matrix(man=[[3,0,2],[2,0,-2],[0,1,1]])
        self.assertEqual(MatOPS.det(A), 10)

if __name__ == "__main__":
    unittest.main()