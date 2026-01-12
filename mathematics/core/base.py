

class Node:
  
  def _ensure_node(self, other):
    if isinstance(other, (int, float)):
      return Constant(other)
    return other
  
  def __add__(self, other):
    other = self._ensure_node(other)
    return Add(self, other)
  
  def __sub__(self, other):
    other = self._ensure_node(other)
    return Subtract(self, other)
  
  def __radd__(self, other):
    return Add(self._ensure_node(other), self)
  
class Constant(Node):
  
  def __init__(self, value):
    self.value = value
  
  def __repr__(self):
    return self.value
  
  def evaluate(self):
        return self.value

class Add(Node):
  
  def __init__(self, left: Constant, right: Constant):
    self.left = left
    self.right = right
  
  def __repr__(self):
    return f"{str(self.left.value)}+{str(self.right.value)}"
  
  def evaluate(self):
    return self.left.evaluate() + self.right.evaluate()
  
class Subtract(Node):
  
  def __init__(self, left: Constant, right: Constant):
    self.left = left
    self.right = right
  
  def evaluate(self):
    return self.left.evaluate() - self.right.evaluate()