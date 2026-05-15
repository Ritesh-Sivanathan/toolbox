from .matrices import Matrix
from copy import deepcopy

class MatOPS:

    @staticmethod
    def gaussian_elimination(matrix:Matrix):
        
        """

        Returns: 
            Determinant and resulting row-echelon form of the original matrix.
            `None` if the matrix cannot be operated on
            0,0 if there is a row or columns of zeroes.
        
            
        """
            
        det = 1
        
        row_swap = False
        found = False

        if isinstance(matrix, Matrix):
            matrix = matrix.matrix

        if not isinstance(matrix, (Matrix, list)):
            return TypeError("Please provide a valid datatype for `matrix`")

        for z in range(len(matrix)):

            if matrix[z][z] == 0:
                
                row_swap = True

                for temp in range(z, len(matrix)):
                    
                    if matrix[temp][z] != 0:
                        
                        t = matrix[z]
                        s = matrix[temp]

                        matrix[temp] = t
                        matrix[z] = s

                        det *= -1

                        found = True

                        break
                
                if row_swap and not found:
                    return 0,0

            for row in range(z+1, len(matrix)):
                
                if matrix[row][z] != 0:

                    factor = matrix[row][z] / matrix[z][z]

                    for nin, element in enumerate(matrix[row]):

                        matrix[row][nin] -= factor*matrix[z][nin]
                            
        for i in range(len(matrix)):
            det *= matrix[i][i]

        return det, Matrix(man=matrix)

    @staticmethod
    def _preprocess(matrix, return_type="list"):
        
        if return_type not in {"list", "matrix"}:
            raise ValueError("The only supported return types are List and Matrix")

        if isinstance(matrix, Matrix) and return_type=="list":
            return matrix.matrix
        
        elif isinstance(matrix, list) and return_type == "matrix":
            return Matrix(man=matrix)
        
        elif (isinstance(matrix, list) and return_type == "list") or (isinstance(matrix, Matrix) and return_type == "matrix"):
            return matrix
        
        else:
            raise TypeError("The provided matrix must be of type List or Matrix")

    @staticmethod
    def dims(matrix):

        """
        
        Returns the dimensions of a matrix represented by lists \\
        Use on `list` type only (`Matrix` type is unsupported for now)

        """

        if not type(matrix) == list:
            return []
        return [len(matrix)] + MatOPS.dims(matrix[0])

    @staticmethod
    def det(matrix:Matrix):

        """
        
        Returns the single value for the determinant of the `Matrix`. \\
        Input: `Matrix` object or a valid square matrix of [nested] lists
        
        """

        matrix = MatOPS._preprocess(matrix, return_type="matrix")

        if matrix.r != matrix.c:
            raise ValueError("Determinant is only defined for square matrices")

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
    
    @staticmethod
    def T(matrix: Matrix):

        """
        
        Transpose a `Matrix` object or in a matrix of [nested] lists
        
        """

        new_matrix = []

        matrix = MatOPS._preprocess(matrix, return_type="matrix")
        
        for c_index in range(matrix.c):

            row = []

            for r_index in range(matrix.r):
                row.append(matrix.matrix[r_index][c_index])
            new_matrix.append(row)
        
        return new_matrix

    @staticmethod
    def cof(matrix):

        """
        
        Returns the Matrix as [nested] arrays for the cofactor matrix of the `Matrix`. \\
        Input: `Matrix` object or a valid square matrix of [nested] lists
        
        """

        matrix = MatOPS._preprocess(matrix, return_type="matrix")

        if matrix.r != matrix.c:
            raise ValueError("Determinant is only defined for square matrices")

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
    
    @staticmethod
    def adjoint(matrix:Matrix):
        
        """

        Returns the adjoint of a `Matrix` or [nested] arrays as [nested] arrays
        Adjoint = T(cof(A))
         
        """

        matrix = MatOPS._preprocess(matrix, return_type="matrix")

            
        if matrix.r != matrix.c:
            raise ValueError("Input matrix must be a square matrix (nxn dimensions)")
            
        return MatOPS.T(MatOPS.cof(matrix))       
    
    @staticmethod
    def inverse(matrix: Matrix, precision=3):
        """
        Returns the inverse of a matrix if it is invertible. \\

        ### Arguments
            
        `matrix`: Matrix to multiply. Must be of type `List` or `Matrix` \\
        `precision` (optional): Floating point precision for result
        
        """

        matrix = MatOPS._preprocess(matrix, return_type="matrix")

        det = MatOPS.det(matrix)

        if det != 0:

            new_matrix = MatOPS.adjoint(matrix)
            return MatOPS.matmul(matrix=new_matrix, scalar=(1/det), precision=precision)

        elif det == 0:
            
            raise ValueError("Matrix must have a non-zero determinant to be inverted.")
        
    @staticmethod
    def MatMul(A, B, precision=3):
        
        if isinstance(A, Matrix) and isinstance(B, Matrix):
        
            Ar, Ac = A.r, A.c
            Br, Bc = B.r, B.c
                    
            if Ac != Br:
                return ValueError("These matrices cannot be multiplied by each other")
            
            output = [[] for _ in range(Ar)]
            
            for row in range(A.r):
                for col in range(B.c):
                    
                    sum = 0
                    target = [B.matrix[r][col] for r in range(Br)]
                    
                    for i in range(len(A.matrix[row])):
                        sum += A.matrix[row][i] * target[i]
                                        
                    output[row].append(sum)
                    
            return Matrix(man=output)

        elif isinstance(A, (float, int)) or isinstance(B, (float, int)):
            
            MatrixA = isinstance(A, Matrix)
            
            constant = B if MatrixA else A
            output = [[] for _ in range(A.r if MatrixA else B.r)]
            matrix = A if MatrixA else B
            
            for r, row in enumerate(matrix.matrix):
                for c, col in enumerate(row):

                    output[r].append(round(col*constant,ndigits=precision))
            
            return Matrix(man=output)