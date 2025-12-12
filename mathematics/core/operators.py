from .base import Constant, Variable

class Add:
  
  def __init__(self, Node1, Node2):
    
    self.Node1 = Node1
    self.Node2 = Node2
  
  def __add__(self, Node3):
    
    return Constant(self.evaluate()) + Constant(Node3.evaluate())
    
  def evaluate(self):
    
    return self.Node1 + self.Node2
  
class Subtract:
  
  def __init__(self, Node1, Node2):
    
    self.Node1 = Node1
    self.Node2 = Node2
    
  def evaluate(self):
    
    return self.Node1 - self.Node2

class Multiply:
  
  def __init__(self, Node1, Node2):
    
    self.Node1 = Node1
    self.Node2 = Node2  
  
  def evaluate(self):
    
    return self.Node1 * self.Node2
  
class Divide:
  
  def __init__(self, Node1, Node2):
    
    self.Node1 = Node1
    self.Node2 = Node2  
  
  def evaluate(self):
    
    return self.Node1 / self.Node2