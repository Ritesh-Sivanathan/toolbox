from core import *

# x = Variable('x')
# y = Variable('y')

# expr = (x**2) * (y**2)
# expr = 3 * x * 3
# expr = 3*x + 2*x
expr = (Constant(1) + Constant(3)) + Constant(2)
expr = Constant(3) * Constant(2) * Constant(4)

print(expr)
print(expr.eval())
