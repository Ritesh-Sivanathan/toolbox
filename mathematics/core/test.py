from core import *

a = Variable('a')
x = Variable('x')
y = Variable('y')
z = Variable('z')

one = Constant(1)
two = Constant(2)

expr = one * x
print(expr.eval())
print(type(expr.eval()))
