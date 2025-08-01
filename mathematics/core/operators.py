from .base import Constant, Variable

class Add:
  
  def __init__(self, val_1, val_2):
    
    self.val_1:Constant = val_1
    self.val_2:Constant = val_2
    self.traverse = True
  
  def evaluate(self):
    
    if (type(self.val_1) == Variable and not self.val_1.value) or (type(self.val_2) == Variable and not self.val_2.value):

      return f"{self.val_1.symbol if type(self.val_1) == Variable else self.val_1.value}+{self.val_2.symbol if type(self.val_2) == Variable else self.val_2.value}"
 
    return self.val_1.value + self.val_2.value
  
  def show(self):
    
    return self.val_1, self.val_2
  
class Subtract:
  
  def __init__(self, val_1, val_2):
    
    self.val_1:Constant = val_1
    self.val_2:Constant = val_2
    self.traverse = True
  
  def evaluate(self):
    
    return self.val_1.value - self.val_2.value
  
  def show(self):  
    
    return self.val_1, self.val_2

class Multiply:
  
  def __init__(self, val_1, val_2):
    
    self.val_1:Constant = val_1
    self.val_2:Constant = val_2
    self.traverse = True
  
  def evaluate(self):
    
    return self.val_1.value * self.val_2.value
  
  def show(self):  
    
    return self.val_1, self.val_2
  
class Divide:
  
  def __init__(self, val_1, val_2):
    
    self.val_1:Constant = val_1
    self.val_2:Constant = val_2
    self.traverse = True
  
  def evaluate(self):
    
    return self.val_1.value / self.val_2.value
  
  def show(self):
    
  	return self.val_1, self.val_2

class Power:
  
  def __init__(self, base, exp):
    
    self.base:Constant = base
    self.exp:Constant = exp
    self.traverse = True
  
  def evaluate(self):
    
    return self.base.value ** self.exp.value
  
  def show(self):
    
    return [self.base, self.exp]
