### Toolbox Core

`gpc()` -> recursive method on the `DataType`, `Add`, and `Multiply` classes. Creates a dictionary of the **expanded** terms in a Node and each of their coefficients. Simplifies the entire thing at the end by scanning through the dictionary, adding or multiplying like terms, and finally, for Multiply nodes, multiplying the remaining terms in each dictionary and their respective coefficients. Final result is a simplified polynomial. This relies heavily on the `expand` method.

`expand()` -> recursive method for expanding polynomial expressions using basic addition and multiplication rules. Critical for simplification logic.

#### Future Changes / To-Dos

1. More consistent formatting for simplification - terms are arranged by their order
2. Extensive testcases for the expansion and simplification logic
3. Clean code - get rid of any deprecated functions and blocks of code, write clear documentation and update docstrings
