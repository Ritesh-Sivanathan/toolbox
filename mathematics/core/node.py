
class Add:

    def __init__(self,left,right):
        self.left=left
        self.right=right

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l + r

class Subtract:

    def __init__(self,left,right):
        self.left=left
        self.right=right

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l - r


class Multiply:

    def __init__(self,left,right):
        self.left=left
        self.right=right

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l * r

class Divide:

    def __init__(self,left,right):
        self.left=left
        self.right=right

    def eval(self):

        l = self.left.eval()
        r = self.right.eval()

        return l / r


class Constant:

    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self,other):
        return Subtract(self,other)

    def __mul__(self,other):

        return Multiply(self,other)

    def __truediv__(self,other):

        return Divide(self,other)

    def eval(self):
        
        if isinstance(self.value, (Add,Multiply)):
            return self.value.eval()

        return self.value
