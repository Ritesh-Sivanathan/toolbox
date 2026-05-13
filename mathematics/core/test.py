from core import *

x = Variable('x')
y = Variable('y')

# expr = (x**2) * (y**2)
# expr = 3 * x * 3
# expr = 3*x + 2*x
expr = x**3 + x**3

print(expr.eval())
