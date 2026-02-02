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

        `mode` *(default="zero")*: Populate all elements of the Matrix with: zeroes ("zero"), empty ("empty"), fill ("fill"), random ("rand") \\
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


    def gaussian_elimination(self):
        
        """

        Returns: 

            Determinant and row-echelon form of `matrix` with its determinant.
            `None` if the matrix cannot be operated on
            (0,0) if matrix is singular

            Does not mutate original matrix
        
        """
            
        determinant = 1
        
        matrix = [[element for element in row] for row in self.matrix]

        for pivot in range(len(matrix)):

            found_swap = False

            if matrix[pivot][pivot] == 0:

                for check_pot_pivot in range(pivot, len(matrix)):
                    
                    if matrix[check_pot_pivot][pivot] != 0:
                        
                        t = matrix[pivot]
                        s = matrix[check_pot_pivot]

                        matrix[pivot], matrix[check_pot_pivot] = matrix[check_pot_pivot], matrix[pivot]

                        matrix[check_pot_pivot] = t
                        matrix[pivot] = s

                        determinant *= -1

                        found_swap = True

                        break
                
                if not found_swap:
                    return 0, 0

            for row in range(pivot+1, len(matrix)):
                
                if matrix[row][pivot] != 0:

                    factor = matrix[row][pivot] / matrix[pivot][pivot]

                    for index, parallel_element in enumerate(matrix[row]):

                        matrix[row][index] -= factor*matrix[pivot][index]
                            
        for i in range(len(matrix)):
            determinant *= matrix[i][i]

        return determinant, Matrix(man=matrix)

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

        sub = [[element for element in row] for row in self.matrix]

        if self.r == 1 and self.c == 1:
            return self.matrix[0][0]

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

        sub = [[element for element in row] for row in self.matrix]

        cofactor_matrix = []
    
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
    
    def __add__(self, other):
        
        if not isinstance(other, Matrix):
            raise TypeError("These types cannot be added together")
        
        if self.r != other.r or self.c != other.c:
            return ValueError("The dimensions of both matrices must be the same to add them")
        
        output = [[] for i in range(self.r)]
        
        for r in range(self.r):
            for c in range(self.c):
                output[r].append(self.matrix[r][c] + other.matrix[r][c])
        
        return Matrix(man=output)
    
    def __rmul__(self, other):
        
        if isinstance(other, Matrix):
            pass
        
        elif isinstance(other, (int, float)):
            return self.__mul__(other)

    def __mul__(self, other, precision=3):

        if isinstance(other, Matrix):
        
            Ar, Ac = self.r, self.c
            Br, Bc = other.r, other.c
                    
            if Ac != Br:
                return ValueError("These matrices cannot be multiplied by each other")
            
            output = [[] for _ in range(Ar)]
            
            for row in range(self.r):
                for col in range(other.c):
                    
                    sum = 0
                    target = [other.matrix[r][col] for r in range(Br)]
                    
                    for i in range(len(self.matrix[row])):
                        sum += self.matrix[row][i] * target[i]
                                        
                    output[row].append(sum)
                    
            return Matrix(man=output)

        elif isinstance(other, (float, int)):
            
            MatrixA = isinstance(self, Matrix)
            
            constant = other
            output = [[] for _ in range(self.r)]
            matrix = self if MatrixA else self
            
            for r, row in enumerate(matrix.matrix):
                for c, col in enumerate(row):

                    output[r].append(round(col*constant,ndigits=precision))
            
            return Matrix(man=output)
    
    __rmul__ = __mul__
    
    def mul(self, target):
        
        if not (isinstance(target, (float,int,Matrix))):
            return ValueError("This datatype is not supported for matrix multiplication")
        
        if isinstance(target, Matrix):
            pass
    
    def is_square(self):

        return self.r == self.c
    
    def show(self):
        
        return self.matrix