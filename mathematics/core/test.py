from node import Add, Multiply, Constant, Term, Variable

x = Variable('x')
y = Variable('y')
# expr = x**0 + y**0 + y
expr = x + y
print(expr.eval())
