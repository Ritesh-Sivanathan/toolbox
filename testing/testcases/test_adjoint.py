from toolbox.mathematics.linear_algebra.matrices import Matrix
from toolbox.mathematics.linear_algebra.MatOPS import MatOPS
import unittest
import sympy

class AdjointTest(unittest.TestCase):

    """
    
    Testing the `adjoint()` function from both the `Matrix` object and the `MatOPS` class
    
    """

    def test_identity_2x2(self):
        
        A = Matrix(man=[[1,0,0],[0,1,0],[0,0,1]])
        B = sympy.Matrix([[1,0,0],[0,1,0],[0,0,1]]).adjugate()

        self.assertEqual(A.adjoint().matrix, B.tolist(), MatOPS.adjoint(A))
    
    def test_random_3x3(self):

        A = Matrix(3,3, mode="rand")
        B = sympy.Matrix(A.matrix).adjugate()

        self.assertEqual(A.adjoint().matrix, B.tolist(), MatOPS.adjoint(A))
    
    def test_random_5x5(self):

        A = Matrix(5,5, mode="rand")
        B = sympy.Matrix(A.matrix).adjugate()

        self.assertEqual(A.adjoint().matrix, B.tolist(), MatOPS.adjoint(A))

if __name__ == "__main__":

    unittest.main()