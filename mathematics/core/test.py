from core import *

# expression = Constant(1) + Constant(2)
x = Variable('x')
y = Variable('y')

print(type(Constant(2)*x**3))

# expression_2 = x**0 + y**0 + x**0 + y**0
expression_3 = Constant(2)*x**3 + 1

print(type(expression_3.eval()))
print(expression_3.eval().left)

# print(expression.eval())
# print(expression_2.eval())
# print(type(expression_3))
# print(expression_3.eval())
# print(expression_3)

