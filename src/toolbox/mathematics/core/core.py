class BinaryOp:

    """

    Binary Operation

    ### Attributes

        self.left -> Node
        self.right -> Node

    ### Methods

        __repr__
        __key__
        __hash__
        __add__
        __radd__
        __mul__
        __rmul__
        __eq__

        poly_count()

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
 
    def poly_count(self) -> dict:

        """

        Collects and counts all polynomial terms.

        Returns a dictionary with the count of each polynomial type.

        *Used for expansion and simplification ops.*

        """
        
        left = self.left.poly_count()
        right = self.right.poly_count()

        simple_polynomial = {}

        for key, val in left.items():

            if key in simple_polynomial:
                simple_polynomial[key] += val # Add the coefficients of like terms
            else:
                simple_polynomial[key] = val

        for key, val in right.items():

            if key in simple_polynomial:
                simple_polynomial[key] += val # Add the coefficients of like terms
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
    
    DataType

    ### Attributes

        `self.value` -> `Int | Node`

    ### Methods

        `expand()`
        `poly_count()`
        `__key__`
        `__hash__`
        `__repr__`
        `__str__`
        `__eq__`
        `__add__`
        `__radd__`
        `__mul__`
        `__rmul__`
        `__eq__`

        `poly_count()`

    """

    def __init__(self,value):
        self.value = value

    def expand(self):
        return self

    def poly_count(self) -> dict:
        
        """

        Collects and counts all polynomial terms.

        Returns a dictionary with the count of each polynomial type.

        *Used for expansion and simplification ops.*

        """

        if isinstance(self.value, int):
            return { 1: self.value }

        return { Variable(self.value): 1 }

    def __key__(self):
        return (self.value)

    def __hash__(self):
        return hash(self.__key__())

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

    ### Attributes

        `self.left` -> Node
        `self.right` -> Node
    
    ### Methods

        `eval()`
        `expand()`
        `__str__`
        `__eq__`

    """

    def eval(self) -> DataType | BinaryOp:

        """

        Returns the result of adding `self.left` and `self.right`.

        Return type may be a `DataType` or a `BinaryOp`.

        """

        l = self.left.eval()
        r = self.right.eval()
        
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

    ### Methods

        `eval()`
        `expand()`
        `poly_count()`
        `__hash__`
        `__str__`
        `__eq__`

    """

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        # TODO: figure out how to make all this manual crap simpler

        if (l == Constant(0) or r == Constant(0)): ## Return 0 if either term is 0
            return Constant(0)

        if isinstance(l,Constant) and l.value == 1: # 1 * r = r
            return r

        if isinstance(r,Constant) and r.value == 1: # l * 1 = l
            return l
 
        if isinstance(l,Constant) and isinstance(r,Constant): # Constant * Constant
            return Constant(l.value * r.value)

        if isinstance(l, Variable) and isinstance(r, Variable): # Variable * Variable

            if l == r:
                return Exponent(l,Constant(2))

        if isinstance(l, Exponent) and isinstance(r, Variable): # Exponent * Variable
            if l.left == r:
                return Exponent(r,(l.right.eval()+1).eval())
        
        if isinstance(l, Variable) and isinstance(r, Exponent): # Variable * Exponent
            if r.left == l:
                return Exponent(l,(r.right.eval()+1).eval())

        if isinstance(l, Exponent) and isinstance(r, Exponent): # Exponent * Exponent
            if l.left == r.left:
                return Exponent(l.left, (l.right + r.right).eval())

        return l * r
    
    def expand(self):

        left = self.left.expand()
        right = self.right.expand()

        if isinstance(left, Add):
            return (left.left * right + left.right * right).expand()

        if isinstance(right, Add):
            return (left*right.left + left*right.right).expand()

        if isinstance(left,(Variable,Constant)) and isinstance(right,(Multiply,Add)):
            return (left*right.left*right.right)

        return left * right

    def poly_count(self) -> dict:

        """

        Collects and counts all polynomial terms.

        Returns a dictionary with the count of each polynomial type.

        *Used for expansion and simplification ops.*

        """

        if isinstance(self.left, (Variable, Exponent)) and isinstance(self.right, Constant):
            return { self.left : self.right.value }

        if isinstance(self.left, Constant) and isinstance(self.right, (Variable, Exponent)):
            return { self.right : self.left.value }

        left = self.left.poly_count()
        right = self.right.poly_count()

        simple_polynomial = {}

        for key, val in left.items():

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

    def __hash__(self):
        return hash((self.__class__.__name__, self.left, self.right))

    def __str__(self):

        return f"({self.left}) * ({self.right})"

    def __eq__(self,other):
        
        if not isinstance(other, Multiply):
            return False

        return (self.left == other.left and self.right == other.right) or (self.left == other.right and self.right == other.left)

class Exponent(BinaryOp):

    """

    Exponentiate a base.

    ### Attributes

        `self.left` -> Node
        `self.right` -> Node

    ### Methods

        eval()
        poly_count()
        expand()
        __hash__
        __str__
        __add__
        __eq__

    """
    
    def eval(self):

        left = self.left.eval()
        right = self.right.eval()

        if right == Constant(0): # left**0 = 0
            return Constant(1)

        if right == Constant(1): # left**1 = left
            return left

        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value ** right.value)

        return left**right
    
    def poly_count(self) -> dict:

        """

        Collects and counts all polynomial terms.

        Returns a dictionary with the count of each polynomial type.

        *Used for expansion and simplification ops.*

        """

        return { Exponent(self.left,self.right): 1 }

    def expand(self):
        return self
   
    def __hash__(self):
        return hash((self.__class__.__name__, self.left, self.right))

    def __str__(self):

        l = self.left
        r = self.right

        return f"({l} ** {r})"

    def __add__(self,other):

        if not isinstance(other, Exponent):
            return Add(self,other)
        
        if self == other: # Exact same nodes
            return Multiply(Constant(2), self) # Return 2*self

    def __eq__(self,other):

        if not isinstance(other, Exponent):
            return False

        return (self.left == other.left and self.right == other.right)

class Constant(DataType):

    """

    Variable object.

    ### Attributes
        
        `self.value` -> int | float

    ### Methods

        `eval` -> Constant

    """

    def eval(self):
        
        return self

class Variable(DataType):

    """

    Variable object.

    ### Attributes
        
        `self.value` -> str

    ### Methods

        `eval` -> Variable

    """

    def eval(self):

        return self 

def ensure_node(node):

    """

    Converts input `node` to a Constant if it is an `int` or `float`. Returns the input `node` otherwise.

    """
    
    if (isinstance(node,(int,float))):
        return Constant(node)

    return node
