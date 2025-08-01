
class Constant:
  
  def __init__(self, value):
    
    self.value = value
    self.traverse = False
    
class Variable:
  
  def __init__(self, symbol, value=None):
    
    self.value = value
    self.symbol = symbol
    self.traverse = False
    
class Expression:
  
  def __init__(self, expression):
    
    self.expression = expression
    self.traverse = True
  
  def evaluate(self):
    
    # Incomplete...
    
    first_part = self.expression.show()
    
    def dig(part):
      
      results = []
      results.append(part)
      
      if part.traverse:
        
        parts = part.show()
        
        for part in parts:
          res = dig(part)
          results.append(res)
                
      return results
    
    print(dig(self.expression))
    
    return 0