import unittest
from core import *

class ConstantBinaryOperations(unittest.TestCase):

    one = Constant(1)
    two = Constant(2)
    three = Constant(3)

    def test_AddConstantConstant(self):
        expr = self.one + self.two
        self.assertEqual(expr, self.three)

class VariableBinaryOperations(unittest.TestCase):

    pass

if __name__ == "__main__":
    unittest.main()
