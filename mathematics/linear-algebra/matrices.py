# define matrix class
# can be used to create an nxk matrix
# should have a description function to give details on matrix in a concise format

class Matrix:

    def __init__(self, n:int, k:int):
        self.n = n
        self.k = k
        self.matrix = [n*[k*[]]]