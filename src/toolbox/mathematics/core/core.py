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

    def __repr__(self):
        return f"{type(self).__name__}({self.left.__repr__()}, {self.right.__repr__()})"
    
    def __key__(self):
        return (self.left, self.right)

    def __hash__(self):
        return hash(self.__key__())

    def get_polynomial_terms(self):
        
        left = self.left.get_polynomial_terms()
        right = self.right.get_polynomial_terms()

        simple_polynomial = {}

        print(f"Left: {self.left}, Right: {self.right}")

        for key, val in left.items():

            print("K", key)
            print("V", val)

            if key in simple_polynomial:
                simple_polynomial[key] += val
            else:
                simple_polynomial[key] = val

        for key, val in right.items():

            if key in simple_polynomial:
                simple_polynomial[key] += val
            else:
                simple_polynomial[key] = val

        return simple_polynomial

    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return self.__add__(other)

    def __mul__(self,other):
        return Multiply(self,other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __eq__(self,other):

        return self.left == other.left and self.right == other.right

class DataType:

    """

    DataType Object

    Consists of all dunder functions for Constant and Variable classes

    """

    def __init__(self,value):
        self.value = value

    def expand(self):
        return self

    def __key__(self):
        return (self.value)

    def __hash__(self):
        return hash(self.__key__())

    def get_polynomial_terms(self):

        if isinstance(self.value, int):
            return { Constant(1): self.value }

        return { Variable(self.value): 1 }

    def __str__(self):
        return (f"{self.value}")
    
    def __repr__(self):

        return f"{type(self).__name__}({self.value})"

    def __eq__(self,other):

        if not isinstance(other, (Constant, Variable)):
            return False

        return self.value == other.value

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self,other):
        return Add(self,other)

    def __mul__(self,other):
        return Multiply(self,other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __pow__(self,exponent):
        return Exponent(self,exponent)

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

    def expand(self):

        return Add(self.left.expand(), self.right.expand())

    def __str__(self):
        
        return f"{self.left} + {self.right}"

    def __eq__(self,other):

        if not isinstance(other, Add):
            return False

        return (self.left == other.left and self.right == other.right) or (self.left == other.right and self.right == other.left)

class Multiply(BinaryOp):

    """

    Multiply the left and right nodes.

    Child of the BinaryOp class

    """

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()
        
        if isinstance(l,Constant) and isinstance(r,Constant):
            return Constant(l.value * r.value)

        if isinstance(l, Variable) and isinstance(r, Variable):

            if l == r:
                return Exponent(l,Constant(2))

        if isinstance(l, Variable) and isinstance(r, Exponent):
            if r.left == l:
                return Exponent(l,r.right.eval()+1)

        return l * r

    def expand(self):

        left = self.left.expand()
        right = self.right.expand()

        if isinstance(left, Add):
            return ((left.left * right) + (left.right * right)).expand()

        if isinstance(right, Add):
            return ((left*right.left) + (left*right.right)).expand()

        return left * right

    def __str__(self):

        return f"({self.left}) * ({self.right})"

    def __eq__(self,other):
        
        if not isinstance(other, Multiply):
            return False

        return (self.left == other.left and self.right == other.right) or (self.left == other.right and self.right == other.left)

class Exponent(BinaryOp): # has many issues - no simplification for addition or multiplication yet
    
    def eval(self):

        left = self.left.eval()
        right = self.right.eval()

        if right == Constant(0):
            return Constant(1)

        if right == Constant(1):
            return left

        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value ** right.value)

        return left**right
    
    def __hash__(self):
        return hash((self.__class__.__name__, self.left, self.right))

    def get_polynomial_terms(self):

        return { Exponent(self.left,self.right): 1 }

    def __str__(self):

        l = self.left
        r = self.right

        return f"({l} ** {r})"

    def __eq__(self,other):

        if not isinstance(other, Exponent):
            return False

        return (self.left == other.left and self.right == other.right)

    def __add__(self,other):

        if not isinstance(other, Exponent):
            return Add(self,other)
        
        if self == other: # exact same exponent
            return Multiply(Constant(2), self) # you get two of them

    def __mul__(self,other):
 
        if not isinstance(other,(Exponent,(Multiply,Exponent))):
            return Multiply(self,other)

        if isinstance(other, Exponent):
            
            if self.other == other.left: # same bases
                pass

        raise NotImplementedError("Multiplication of exponents is not implemented yet")

        # TODO: mul implementation

    def __rmul__(self,other):
        return self.__mul__(other)

    # TODO: __add__ method

class Constant(DataType):

    def eval(self):
        
        return self

class Variable(DataType):

    def eval(self):

        return self 

def ensure_node(node):
    
    if (isinstance(node,(int,float))):
        return Constant(node)

    return node
