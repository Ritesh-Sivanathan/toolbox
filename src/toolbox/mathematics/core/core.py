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
 
    def __add__(self,other):
        return Add(self,other)

    def __radd__(self,other):
        return self.__add__(other)

    def __sub__(self,other):
        return Add(self,-other)

    def __rsub__(self,other):
        return Add(other,-self)

    def __mul__(self,other):

        return Multiply(self,other)

    def __rmul__(self,other):

        return Multiply(other, self)

    def __eq__(self,other):

        return self.left == other.left and self.right == other.right

    def __neg__(self):
        
        return -1 * self

class DataType:

    """
    
    DataType

    ### Attributes

        `self.value` -> `Int | Node`

    ### Methods

        `expand()`
        `__key__`
        `__hash__`
        `__repr__`
        `__str__`
        `__neg__`
        `__eq__`
        `__add__`
        `__radd__`
        `__sub__`
        `__mul__`
        `__rmul__`
        `__eq__`

    """

    def __init__(self,value):
        self.value = value

    def expand(self):
        return self

    def construct_tree(self):
        
        if isinstance(self, Constant):
            return { Constant(1): self.value }

        return { self: 1 }

    def __neg__(self):

        if isinstance(self, Variable):
            return Constant(-1) * self

        return Constant(-1*self.value)

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

    def __sub__(self,other):
        return Add(self,-other)

    def __rsub__(self,other):
        return Add(-self,other)

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

        `simplify()`
        `expand()`
        `__str__`
        `__eq__`

    """

    def simplify(self) -> DataType | BinaryOp:

        """

        Returns the result of adding `self.left` and `self.right`.

        Return type may be a `DataType` or a `BinaryOp`.

        """

        l = self.left.simplify()
        r = self.right.simplify()
        
        if isinstance(l,Constant) and isinstance(r,Constant):
            return Constant(l.value + r.value)        
 
        if -1*l == r or l*-1 == r: # so it works for a general class
            return Constant(0)

        if l == Constant(0):
            return r
        
        if r == Constant(0):
            return l

        return Add(l,r)

    def construct_tree(self):

        left = self.left.expand().simplify().construct_tree()
        right = self.right.expand().simplify().construct_tree()

        simplified_tree = {}

        for key, value in left.items():
            
            if key in simplified_tree:
                new_val = simplified_tree[key] + value
                del simplified_tree[key]
                simplified_tree[key] = new_val

            elif key not in simplified_tree:
                simplified_tree[key] = value

        for key, value in right.items():
            
            if key in simplified_tree:
                new_val = simplified_tree[key] + value
                del simplified_tree[key]
                simplified_tree[key] = new_val

            elif key not in simplified_tree:
                simplified_tree[key] = value 

        return simplified_tree

    def expand(self):

        return self.left.expand() + self.right.expand()

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

        `simplify()`
        `expand()`
        `__hash__`
        `__str__`
        `__eq__`

    """

    def construct_tree(self):

        left = self.left.expand().simplify().construct_tree()
        right = self.right.expand().simplify().construct_tree()

        simplified_tree = {}

        # Tree simplification logic 

        for key, value in left.items():

            if key in simplified_tree:
            
                new_key = (key*key).simplify()
                new_val = simplified_tree[key] * value

                del simplified_tree[key]

                simplified_tree[new_key] = new_val
            
            elif key not in simplified_tree:
                simplified_tree[key] = value

        for key, value in right.items():

            if key in simplified_tree:
            
                new_key = (key*key).simplify()
                new_val = simplified_tree[key] * value
                
                del simplified_tree[key]

                simplified_tree[new_key] = new_val

            elif key not in simplified_tree:
                simplified_tree[key] = value

        if Constant(1) in simplified_tree:
            scalar = simplified_tree[Constant(1)]
            del simplified_tree[Constant(1)]
            for key, val in simplified_tree.items():
                simplified_tree[key] = val * scalar

        # TEMPORARY CODE
        # TODO: make this neater!

        new_tree = {}
        sole_key=None

        for key, value in simplified_tree.items():
            if len(new_tree) == 0 and key:
                new_tree[key] = value
                sole_key=key
            else:
                new_key = sole_key * key
                new_val = new_tree[sole_key] * value
                del new_tree[sole_key]
                sole_key = new_key
                new_tree[new_key] = new_val

        return new_tree

    def simplify(self):

        l = self.left.simplify()
        r = self.right.simplify()

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
                return Exponent(r,(l.right.simplify()+1).simplify())
        
        if isinstance(l, Variable) and isinstance(r, Exponent): # Variable * Exponent
            if r.left == l:
                return Exponent(l,(r.right.simplify()+1).simplify())

        if isinstance(l, Exponent) and isinstance(r, Exponent): # Exponent * Exponent
            if l.left == r.left:
                return Exponent(l.left, (l.right + r.right).simplify())

        return Multiply(l,r)
    
    def expand(self):

        left = self.left.expand()
        right = self.right.expand()

        if isinstance(left, Add):
            return (left.left * right + left.right * right).expand()

        if isinstance(right, Add):
            return (left*right.left + left*right.right).expand()

        # if isinstance(left,(Variable,Constant)) and isinstance(right,(Multiply,Add)):
           #  return (left*right.left*right.right).expand()

        return Multiply(left,right)

    def __hash__(self):
        return hash((self.__class__.__name__, self.left, self.right))

    def __str__(self):

        return f"({self.left}) * ({self.right})"

    def __neg__(self):
        return -1 * self 

    def __eq__(self,other):
        
        if not isinstance(other, Multiply):
            return False

        return (self.left == other.left and self.right == other.right) or (self.left == other.right and self.right == other.left)

class Exponent(BinaryOp):

    """

    Exponentiate a base.

    ### Attributes

        `self.left` -> Nod
        `self.right` -> Node

    ### Methods

        simplify()
        expand()
        __hash__
        __str__
        __add__
        __eq__

    """
    
    def simplify(self):

        left = self.left.simplify()
        right = self.right.simplify()

        if right == Constant(0): # left**0 = 0
            return Constant(1)

        if right == Constant(1): # left**1 = left
            return left

        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value ** right.value)

        return left**right
    
    def expand(self):
        return self

    def construct_tree(self):
        return { self: 1 }

    def __hash__(self):
        return hash((self.__class__.__name__, self.left, self.right))

    def __str__(self):

        l = self.left
        r = self.right

        return f"({l} ** {r})"

    def __add__(self,other):
 
        if self == other: # Exact same nodes
            return Multiply(Constant(2), self) # Return 2*self

        return Add(self,other)

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

        `simplify` -> Constant

    """

    def simplify(self):
        
        return self

class Variable(DataType):

    """

    Variable object.

    ### Attributes
        
        `self.value` -> str

    ### Methods

        `simplify` -> Variable

    """

    def simplify(self):

        return self 

def ensure_node(node):

    """

    Converts input `node` to a Constant if it is an `int` or `float`. Returns the input `node` otherwise.

    """
    
    if (isinstance(node,(int,float))):
        return Constant(node)

    return node

def reconstruct_tree(tree):

    expr = Constant(0)

    for key, value in tree.items():
        expr += (value * key).simplify()

    return expr.simplify()
