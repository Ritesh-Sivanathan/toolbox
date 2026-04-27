from node import Add, Multiply, Constant, Term, Variable

x = Variable('x')
expr = x + x**3
print(expr.eval())
