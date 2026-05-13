class BinaryOp:

    """

    Binary Operation. All binary operations inherit methods and properties from this class.

    Properties/Attributes:

        `self.left` (`Node`)
        `self.right` (`Node`)

    Ensures both the right and left nodes are actually nodes.

    Currently implemented methods for BinaryOps:

    - Add
    - Multiply
    - Equivalence

    """

    def __init__(self,left,right):
        self.left=ensure_node(left)
        self.right=ensure_node(right)

    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return self.__add__(other)

    def __mul__(self,other):
        return Multiply(self,other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __eq__(self,other):

        return (self.left == other.left, self.right == other.right)


class Add(BinaryOp):

    """

    Add the left and right nodes.

    Child of BinaryOp class.

    """

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l + r

    def __str__(self):
        
        return f"({self.left} + {self.right})"

    def __add__(self,other):

        other = ensure_node(other)

        return Add(self,other)

    def __radd__(self,other):

        other = ensure_node(other)

        return Add(self,other)

    def __mul__(self,other):
        return Multiply(self, other)

    def __rmul__(self,other):
        return self.__mul__(other)

class Multiply(BinaryOp):

    def eval(self):

        l = ensure_node(self.left.eval())
        r = ensure_node(self.right.eval())

        return l * r

    def __str__(self):

        return f"{self.left.eval()} * {self.right.eval()}"

    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return Add(self,other)

    def __mul__(self,other):
        return Multiply(self,other)

    def __rmul__(self,other):
        return self.__mul__(other)


class Divide(BinaryOp):

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l / r

class Exponent(BinaryOp): # has many issues - no simplification for addition or multiplication yet
    
    def eval(self):

        left = self.left.eval()
        right = self.right.eval()

        if (right==0):
            return Constant(1)

        if (right==1):
            return left

        return left**right

    def __str__(self):

        l = self.left
        r = self.right

        return f"{l} ** {r}"

    def __mul__(self,other):

        if (isinstance(other,Constant)):
            return Multiply(other,self)

        if (isinstance(other, Exponent)): # for now, the implementation will just ignore nested exponents (like if other.right is Multiply(Add(Exponent('x'),Exponent('x')) or something

            if (isinstance(other.eval(),Exponent)):

                if (self.right.eval() == other.right.eval()) and (self.left.eval() == other.left.eval()):

                    return Exponent(self.left, other.eval().right + self.right)
                else:
                    return Multiply(self,other)

        return Constant(1)

    def __rmul__(self,other):
        return self.__mul__(other)

    # TODO: __add__ method

class Constant:

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)

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

    def __pow__(self,exp):
        return Exponent(self,exp)

    def eval(self):
        
        if isinstance(self.value, (int, float)):
            return self.value

        return self.value.eval()

class Variable:

    def __init__(self,symbol):
        self.symbol=symbol

    def __mul__(self,other):
        return Multiply(self,other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return Add(self,other)

    def __pow__(self,exponent):

        return Exponent(self,exponent)

    def eval(self):

        return self

    def __str__(self):

        return f"{self.symbol}"

def ensure_node(node):

    if (isinstance(node,(int,float))):
        return Constant(node)

    return node
