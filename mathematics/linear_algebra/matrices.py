# define matrix class
# can be used to create an nxk matrix
# should have a description function to give details on matrix in a concise format

import random
from copy import deepcopy

class Matrix:

    def __init__(self, r:int=None, c:int=None, mode:str='zero', fill:int=0, man=None):

        '''

        `Matrix` object of `r*c` dimensions, where `r` is the number of rows and `c` is the number of columns.

        ### Required Arguments
        
        `r`: Number of **rows** in the Matrix \\
        `c`: Number of **columns** in the Matrix
        
        ### Optional arguments:

        `mode` *(default="zero")*: Populate all elements of the Matrix with: zeroes ("zero"), empty ("empty"), fill ("fill") \\
        `fill` *(default=0)*: If using `mode="fill"`, populates Matrix with real number `fill`
        
        '''
        
        if man:
            
            res = Matrix.dims(man)

            self.r = res[0]
            self.c = res[1]

            self.matrix = man
            self.mode = "man"

            return
        
        if mode not in {"zero", "empty", "fill", "rand"}:
            raise ValueError(f"Unsupported mode '{mode}'. Use 'zero', 'empty', 'rand', or 'fill'.")

        self.r = r
        self.c = c

        self.mode = mode
        self.fill = fill

        if mode =="zero":
            self.matrix = [[0 for _ in range(c)] for _ in range(r)]
        elif mode == "empty":
            self.matrix = [[None for _ in range(c)] for _ in range(r)]
        elif mode =="fill":
            self.matrix = [[fill for _ in range(c)] for _ in range(r)]
        elif mode == "rand":
            self.matrix = [[random.randint(0,5) for _ in range(c)] for _ in range(r)]

    def __repr__(self):
        return f'Matrix({self.r}, {self.c}, "{self.mode if self.mode else "man"}")'

    @staticmethod
    def dims(matrix):

        """
        
        Returns the dimensions of a matrix represented by lists \\
        Use on `list` type only (`Matrix` type is unsupported for now)

        """
      
        if not isinstance(matrix, list):
            return []
        if not matrix:
            return [0]
        return [len(matrix)] + Matrix.dims(matrix[0])
    
    def det(self):

        """
        
        Returns the single value for the determinant of the `Matrix`. \\
        
        """

        if self.r != self.c:
            raise ValueError("Determinant is only defined for square matrices")

        det = 0

        sub = deepcopy(self.matrix)

        if self.r == 2 and self.c == 2:
            return ((sub[0][0]*sub[1][1]) - (sub[0][1]*sub[1][0]))
    
        elif self.r == self.c > 2:

            for i,j in enumerate(sub[0]):
                
                t = deepcopy(sub)[1:]

                for k,r in enumerate(t):
                    del t[k][i]
                            
                res = Matrix(man=t).det()

                if type(res) == int:
                    det += ((-1) ** i) * j * res # cofactor

        return det

    def T(self):

        """
        
        Transpose `Matrix` object
        
        """

        new_matrix = []
        
        for c_index in range(self.c):

            row = []

            for r_index in range(self.r):
                row.append(self.matrix[r_index][c_index])

            new_matrix.append(row)
        
        return Matrix(man=new_matrix)
    
    def cof(self):

        """
        
        Returns the Matrix as [nested] arrays for the cofactor matrix of the `Matrix`. \\
        Input: `Matrix` object or a valid square matrix of [nested] lists
        
        """

        if self.r != self.c:
            raise ValueError("Determinant is only defined for square matrices")

        det = 0

        sub = deepcopy(self.matrix)

        cofactor_matrix = []

        if self.r == 2 and self.c == 2:
            return ((sub[0][0]*sub[1][1]) - (sub[0][1]*sub[1][0]))
    
        for r_index, row in enumerate(sub):

            row_cof_matrix = []

            for c_index, col_element in enumerate(row):

                t = deepcopy(sub)
                t.pop(r_index)
                
                for k,r in enumerate(t):
                    del t[k][c_index]
                
                res = Matrix(man=t).det()
                row_cof_matrix.append(res*((-1)**(c_index+(r_index*3))))
            
            cofactor_matrix.append(row_cof_matrix)
        
        return Matrix(man=cofactor_matrix)

    def adjoint(self):
        
        """

        Returns the adjoint of a `Matrix` or [nested] arrays as [nested] arrays
        Adjoint = T(cof(A))
         
        """
            
        if self.r != self.c:
            raise ValueError("Input matrix must be a square matrix (nxn dimensions)")

        return self.cof().T()

    def inverse(self, precision=3):

        """
        Returns the inverse of a matrix if it is invertible. \\

        ### Arguments
            
        `matrix`: Matrix to multiply. Must be of type `List` or `Matrix` \\
        `precision` (optional): Floating point precision for result
        
        """

        det = self.det()

        if det == 0:
            raise ValueError("Matrix must have a non-zero determinant to be inverted.")

        new_matrix = self.adjoint()
        return new_matrix * (1/det)
            

    def __mul__(self, scalar, precision=3):

        """

        Only supported for scalar by matrix multiplication (for now)
        
        """

        matrix = deepcopy(self.matrix)

        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                matrix[r][c] = round(col*scalar,ndigits=precision)
        
        return Matrix(man=matrix)