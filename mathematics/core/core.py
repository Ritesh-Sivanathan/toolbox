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

    Child of the BinaryOp class.

    """

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        
        # this feels really iffy... but it works for now - will get rid of specific type checks for returns later

        if isinstance(l,Constant) and isinstance(r,Constant):
           return Constant(l.value + r.value)

        return l + r

    def __str__(self):
        
        return f"({self.left} + {self.right})"

    def __repr__(self):
        
        return f"Add({self.left.__repr__()}, {self.right.__repr__()})"

    def __eq__(self,other):

        if not isinstance(other, Add):
            return False

        return (self.left == other.left and self.right == other.right) or (self.left == other.right and self.right == other.left)

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

    """

    Multiply the left and right nodes.

    Child of the BinaryOp class

    """

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()
        
        if isinstance(l,(int,float)) and isinstance(r,(int,float)):
            return Constant(l*r)

        return l * r

    def __str__(self):

        return f"{self.left} * {self.right}"

    def __repr__(self):

        return f"Multiply({self.left.__repr__()}, {self.right.__repr__()})"

    def __eq__(self,other):
        
        if not isinstance(other, Multiply):
            return False

        return (self.left == other.left and self.right == other.right) or (self.left == other.right and self.right == other.left)

    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return Add(self,other)

    def __mul__(self,other):

        return Multiply(self,other)

    def __rmul__(self,other):
        return self.__mul__(other)


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

    def __repr__(self):

        return f"Exponent({self.left.__repr__()},{self.right.__repr__()})"

    def __eq__(self,other):

        if not isinstance(other, Exponent):
            return False

        return (self.left == other.left and self.right == other.right)

    def __mul__(self,other):

        if (isinstance(other,Constant)):
            return Multiply(other,self)

        # TODO: mul implementation

    def __rmul__(self,other):
        return self.__mul__(other)

    # TODO: __add__ method

class Constant:

    def __init__(self,value):
        self.value = value

    def eval(self):
        
        return self

        # if isinstance(self.value, (int, float)):
            # return self.value

        # return self.value.eval()

    def __str__(self):
        return str(self.value)

    def __repr__(self):

        return f"Constant({self.value})"

    def __eq__(self,other):

        if not isinstance(other, Constant):
            return False

        return self.value == other.value

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

class Variable:

    def __init__(self,symbol):
        self.symbol=symbol
    
    def __str__(self):
        return f"{self.symbol}"

    def __repr__(self):
        return f"Variable('{self.symbol}')"

    def __mul__(self,other):
        return Multiply(self,other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return self.__add__(other)

    def __pow__(self,exponent):

        return Exponent(self,exponent)

    def eval(self):

        return self

def ensure_node(node):
    
    if (isinstance(node,(int,float))):
        return Constant(node)

    return node
