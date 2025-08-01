
class Constant:
  
  def __init__(self, value):
    
    self.value = value

    
class Variable:
  
  def __init__(self, symbol, value=None):
    
    self.value = value
    self.symbol = symbol