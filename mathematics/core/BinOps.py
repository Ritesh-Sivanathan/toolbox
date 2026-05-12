from Utils import ensure_node
from Core import *

class BinaryOp:

    def __init__(self,left,right):
        self.left=ensure_node(left)
        self.right=ensure_node(right)

class Add(BinaryOp):

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l + r

    def __str__(self):
        
        return f"{self.left.eval()} + {self.right.eval()}"

    def __add__(self,other):

        other = ensure_node(other)

        return Add(self.eval(),other.eval())

    def __radd__(self,other):

        other = ensure_node(other)

        return Add(self.eval(),other.eval())

class Multiply(BinaryOp):

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l * r

class Divide(BinaryOp):

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l / r

class VarMul(BinaryOp):

    def eval(self):

        if (isinstance(self.left.eval(), Variable) and isinstance(self.right.eval(), Variable)):
            if self.left.eval().symbol == self.right.eval().symbol:
                return Variable(self.left.symbol, self.left.eval().order+self.right.eval().order)

        return Term(self.left.eval(),self.right.eval()) # what is the point of this?

    def __mul__(self,other):
        return Multiply(self,other).eval()

class VarPow:

    def __init__(self,variable,exponent):
        self.variable=variable
        self.exponent=exponent

    def __mul__(self,other):
        return self.eval() * other 

    def __add__(self,other):
        return Add(self.eval(), other.eval())

    def __radd__(self,other):
        return Add(self.eval(), other.eval())

    def eval(self):

        if (self.exponent == 0):
            return Constant(1)

        return Variable(self.variable.symbol, self.variable.order * self.exponent)
