class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def evaluate(self):
        
        if not self.left or not self.right:
            return self
       
