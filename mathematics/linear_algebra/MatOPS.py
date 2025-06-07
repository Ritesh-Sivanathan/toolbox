from .matrices import Matrix
from copy import deepcopy

class MatOPS:

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
    def matmul(matrix: Matrix, scalar=None, precision=3):

        """

        Only supported for scalar by matrix multiplication (for now)

        ``
        
        """
        
        if type(matrix) == Matrix:
            matrix = deepcopy(matrix.matrix)

        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                matrix[r][c] = round(col*scalar,ndigits=precision)
        
        return matrix
    
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