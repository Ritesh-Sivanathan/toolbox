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
            
            res = MatOPS.dims(man)

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

    def show(self):

        """
        
        Returns string in this format:
            `rows x cols`
        
        """

        return f"{self.r}x{self.c}"

class MatOPS:

    def dims(matrix):

        """
        
        Returns the dimensions of a matrix represented by lists \\
        Use on `list` type only (`Matrix` type is unsupported for now)

        """

        if not type(matrix) == list:
            return []
        return [len(matrix)] + MatOPS.dims(matrix[0])


    def det(matrix:Matrix):

        """
        
        Returns the single value for the determinant of the `Matrix`. \\
        Input: `Matrix` object or a valid square matrix of [nested] lists
        
        """

        if type(matrix) == list:
            
            matrix = Matrix(man=matrix)

            if matrix.r != matrix.c:
                raise ValueError("Determinant is only defined for square matrices")

        elif type(matrix) != Matrix:

            raise TypeError("Input must be a square Matrix object or a list of lists")

        det = 0

        sub = deepcopy(matrix.matrix)

        if matrix.r == 2 and matrix.c == 2:
            return ((sub[0][0]*sub[1][1]) - (sub[0][1]*sub[1][0]))
    
        elif matrix.r == matrix.c > 2:

            for i,j in enumerate(sub[0]):
                
                t = deepcopy(sub)[1:]

                for k,r in enumerate(t):
                    del t[k][i]
                            
                res = MatOPS.det(Matrix(man=t))

                if type(res) == int:
                    det += ((-1) ** i) * j * res # cofactor

        return det
    
    def T(matrix: Matrix):

        """
        
        Transpose a `Matrix` object or in a matrix of [nested] lists
        
        """

        new_matrix = []

        if type(matrix) == list:
            matrix = Matrix(man=matrix)
        
        for c_index in range(matrix.c):

            row = []

            for r_index in range(matrix.r):
                row.append(matrix.matrix[r_index][c_index])
            new_matrix.append(row)
        
        return new_matrix

    def cof(matrix):

        """
        
        Returns the Matrix as [nested] arrays for the cofactor matrix of the `Matrix`. \\
        Input: `Matrix` object or a valid square matrix of [nested] lists
        
        """

        if type(matrix) == list:
            
            matrix = Matrix(man=matrix)

            if matrix.r != matrix.c:
                raise ValueError("Determinant is only defined for square matrices")

        elif type(matrix) != Matrix:

            raise TypeError("Input must be a square Matrix object or a list of lists")

        det = 0

        sub = deepcopy(matrix.matrix)

        cofactor_matrix = []

        if matrix.r == 2 and matrix.c == 2:
            return ((sub[0][0]*sub[1][1]) - (sub[0][1]*sub[1][0]))
    
        for r_index, row in enumerate(sub):

            row_cof_matrix = []

            for c_index, col_element in enumerate(row):

                t = deepcopy(sub)
                t.pop(r_index)
                
                for k,r in enumerate(t):
                    del t[k][c_index]
                
                res = MatOPS.det(t)
                row_cof_matrix.append(res*((-1)**(c_index+(r_index*3))))
            
            cofactor_matrix.append(row_cof_matrix)
        
        return cofactor_matrix
    
    def adjoint(matrix:Matrix):
        
        """

        Returns the adjoint of a `Matrix` or [nested] arrays as [nested] arrays
        Adjoint = T(cof(A))
         
        """

        if type(matrix) == list:
            
            matrix = Matrix(man=matrix)
            
            if matrix.r != matrix.c:
                raise ValueError("Input matrix must be a square matrix (nxn dimensions)")
            
        elif type(matrix) != Matrix:
            raise TypeError("Must provide either an array or Matrix object as input.")
    
        return MatOPS.T(MatOPS.cof(matrix))