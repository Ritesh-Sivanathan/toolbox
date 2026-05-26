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

    def test_BinOpsMultipleNestedConstants(self):
        expr = (Constant(1) + (Constant(3)+Constant(2))) + (Constant(2)*(Constant(3)*Constant(2)))
        self.assertEqual(expr.eval(),Constant(18))

class VariableBinOps(unittest.TestCase):

    a = Variable('a')
    b = Variable('b')
    c = Variable('c')
    x = Variable('x')
    y = Variable('y')
    z = Variable('z')

    def test_SimpleVarAdd(self):
        expr = self.a + self.b
        self.assertEqual(expr.eval(),Add(self.a,self.b))

    def test_SimpleVarMul(self):
        expr = self.a * self.b
        self.assertEqual(expr.eval(),Multiply(self.a,self.b))

    def test_SimplifyVarMul(self):
        expr = self.a * self.a
        self.assertEqual(expr.eval(),Exponent(self.a, Constant(2)))

''' Expand is still in development - uncomment after done

class TestExpand(unittest.TestCase):

    e1 = (x + Constant(3)) * (x + Constant(2))
    e2 = (x) * (x + Constant(2))
    e3 = (x + Constant(3)) * x
    e4 = (x + Constant(2)) * (x*y)

    with self.subTest():
        self.assertEqual(self.e1.expand(), ...)

'''

class ConstantUnaryOperations(unittest.TestCase):

    def test_ConstantPowConstant(self):
        expr = Constant(2) ** Constant(2)
        self.assertEqual(expr.eval(), Constant(4))

if __name__ == "__main__":
    unittest.main()
