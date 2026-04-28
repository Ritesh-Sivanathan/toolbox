def _ensure_node(node):

    if (isinstance(node,(int,float))):
        print("check")
        return Constant(node)

    return node

class Add:

    def __init__(self,left,right):

        self.left=_ensure_node(left)
        self.right=_ensure_node(right)

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l + r

    def __repr__(self):
        
        return f"{self.left.eval()} + {self.right.eval()}"

class Multiply:

    def __init__(self,left,right):
        self.left=_ensure_node(left)
        self.right=_ensure_node(right)

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l * r

class Divide:

    def __init__(self,left,right):
        self.left=_ensure_node(left)
        self.right=_ensure_node(right)

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l / r


class Constant:

    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self,other):
        return Subtract(self,other)

    def __mul__(self,other):

        return Multiply(self,other)

    def __truediv__(self,other):

        return Divide(self,other)

    def eval(self):
        
        if isinstance(self.value, (Add,Multiply)):
            return self.value.eval()

        return self.value

class Term:

    def __init__(self,variable,coefficient):
        self.variable = variable
        self.coefficient = coefficient
    
    def __add__(self, other):
        
        if (self.variable==other.variable):
            return Term(self.variable,self.coefficient+other.coefficient)
        else:

            return (self, other)

    def __repr__(self):
        return f"{self.variable.symbol}: {self.coefficient}"

class VarMul:

    def __init__(self,left,right):
        self.left=_ensure_node(left)
        self.right=_ensure_node(right)

    def eval(self):

        if (isinstance(self.left.eval(), Variable) and isinstance(self.right.eval(), Variable)):
            if self.left.eval().symbol == self.right.eval().symbol:
                return Variable(self.left.symbol, self.left.eval().order+self.right.eval().order)

        return Term(self.left.eval(),self.right.eval())

class VarPow:

    def __init__(self,variable,exponent):
        self.variable=variable
        self.exponent=exponent

    def __mul__(self,other):
        return self.eval() * other 

    def __add__(self,other):
        return VarAdd(self.eval(), other.eval())

    def eval(self):

        if (self.exponent == 0):
            return Constant(1)

        return Variable(self.variable.symbol, self.variable.order * self.exponent)

class VarAdd:

    def __init__(self,left,right):
        self.left=_ensure_node(left)
        self.right=_ensure_node(right)

    def eval(self):

        return self.left.eval() + self.right.eval()

    def __add__(self,other):
        return VarAdd(self.eval(),other.eval())

    def __repr__(self):
        return f"{self.left} + {self.right}"


class Variable:

    def __init__(self,symbol,order=1):
        self.symbol=symbol
        self.order=order

    def __mul__(self,other):
        return VarMul(self,other)

    def __add__(self,other):
        return VarAdd(self,other)

    def __pow__(self,exponent):
        return VarPow(self,exponent)

    def eval(self):

        if (self.order == 0):
            return Constant(1)
        return self

    def __repr__(self):

        return f"{self.symbol}{'^' + str(self.order) if self.order != 1 else ''}"
