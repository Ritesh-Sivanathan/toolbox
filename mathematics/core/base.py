class Expression:
          
  def to_string(self):
    pass
  
  def evaluate(self, environment):
    
    for index, expression in enumerate(self.expression):
      print(expression)
      
  def simplify(self):
    pass

class Constant(Expression):
  
  def __init__(self, value):
    
    self.value = value
    self.traverse = False
    
  def __repr__(self):
    
    return str(self.value)

  def __neg__(self):
    
    return Constant(-self.value)
    
  def __add__(self, value):
    
    if isinstance(value, Constant):
      sum = Constant(self.value + value.value)
      return sum
    
    if isinstance(value, (int, float)):
      sum = Constant(self.value + value)
      return sum
    
    raise ValueError("Cannot add type `Constant` to provided type")
  
  def __sub__(self, value):
    
    if isinstance(value, Constant):
      sum = Constant(self.value - value.value)
      return sum
    
    if isinstance(value, (int, float)):
      sum = Constant(self.value - value)
      return sum
    
    raise ValueError("Cannot subtract type `Constant` from provided type")
  
  def __mul__(self, value):
    
    if isinstance(value, Constant):
      sum = Constant(self.value * value.value)
      return sum
    
    if isinstance(value, (int, float)):
      sum = Constant(self.value * value)
      return sum
    
    raise ValueError("Cannot multiply type `Constant` to provided type")
  
  def __truediv__(self, value):
    
    if isinstance(value, Constant):
      sum = Constant(self.value / value.value)
      return sum
    
    if isinstance(value, (int, float)):
      sum = Constant(self.value / value)
      return sum
    
    raise ValueError("Cannot divide type `Constant` by provided type")
  
  def evaluate(self):
    
    return self.value
  
  # Overloaded Operators
  
  def __radd__(self, value):
    
    node = Constant(value)
    
    return self.__add__(node)
  
  def __rsub__(self, value):
    
    node = Constant(value)
    
    return self.__sub__(node)
  
  def __rmul__(self, value):
    
    node = Constant(value)
    
    return self.__mul__(node)
  
  def __rtruediv__(self, value):
    
    numerator_node = Constant(value)
    
    return self.__truediv__(numerator_node)
  
class Variable:
  
  def __init__(self, symbol, value=None):
    
    self.value = value
    self.symbol = symbol
    self.traverse = False
    
