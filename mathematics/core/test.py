from core import *

a = Variable('a')
x = Variable('x')
y = Variable('y')
z = Variable('z')

expr = Constant(2) ** Constant(2)
print(expr.eval())
