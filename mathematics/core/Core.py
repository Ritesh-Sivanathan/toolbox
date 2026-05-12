from Utils import ensure_node
from BinOps import *

class Constant:

    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self,other):
        return Add(self,other)

    def __sub__(self,other):
        return Subtract(self,other)

    def __mul__(self,other):
        return Multiply(self,other)

    def __truediv__(self,other):
        return Divide(self,other)

    def eval(self):
        
        if isinstance(self.value, (int, float)):
            return self.value

        return self.value.eval()

class Operator:

    def __add__(self,other):
        other = ensure_node(other) 
        return Add(self,other)

    def __radd__(self,other):
        other = ensure_node(other)
        return Add(self,other)

class Term:

    def __init__(self,variable,coefficient):
        self.variable = variable
        self.coefficient = coefficient
    
    def __add__(self, other):
        
        if (self.variable==other.variable):
            return Term(self.variable,self.coefficient+other.coefficient)
        else:

            return (self, other)

    def __str__(self):
        return f"{self.variable.symbol}: {self.coefficient}"

class Variable:

    def __init__(self,symbol,order=1):
        self.symbol=symbol
        self.order=order

    def __mul__(self,other):
        return VarMul(self,other)

    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return Add(self,other)

    def __pow__(self,exponent):
        return VarPow(self,exponent)

    def eval(self):

        if (self.order == 0):
            return Constant(1)
        return self

    def __str__(self):

        return f"{self.symbol}{'^' + str(self.order) if self.order != 1 else ''}"
