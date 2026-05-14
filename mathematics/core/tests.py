import unittest
from core import *

class ConstantBinaryOperations(unittest.TestCase):

    a = Variable('a')
    b = Variable('b')
    c = Variable('c')
    x = Variable('x')
    y = Variable('y')
    z = Variable('z')

    def test_AddConstantConstant(self):
        expr = Constant(1) + Constant(2)
        self.assertEqual(expr.eval(), Constant(3))

    def test_AddNestedConstantConstant(self):
        expr = (Constant(1) + Constant(2)) + Constant(3)
        self.assertEqual(expr.eval(), Constant(6))

    def test_AddConstantAndVariable(self):
        expr = Constant(1) + self.x
        self.assertEqual(expr.eval(), Add(Constant(1), Variable('x')))

class ConstantUnaryOperations(unittest.TestCase):

    def test_ConstantPowConstant(self):
        expr = Constant(2) ** Constant(2)
        self.assertEqual(expr.eval(), Constant(4))

if __name__ == "__main__":
    unittest.main()
