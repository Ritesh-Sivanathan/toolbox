from ..linear_algebra.matrices import Matrix

def gaussian(matrix):

    d = 1

    if isinstance(matrix, Matrix):
        matrix = matrix.matrix

    for z in range(len(matrix)):

        # WIP (row swaps)

        if matrix[z][z] == 0:
            
            for temp in range(len(matrix)):
                if matrix[temp][z] != 0:
                    
                    t = matrix[z]
                    s = matrix[temp]

                    matrix[temp] = t
                    matrix[z] = s

        for row in range(z+1, len(matrix)):
            
            if matrix[row][z] != 0:

                factor = matrix[row][z] / matrix[z][z]

                for nin, element in enumerate(matrix[row]):

                    matrix[row][nin] -= factor*matrix[z][nin]
                        
    for i in range(len(matrix)):
        d *= matrix[i][i]

    return d, Matrix(man=matrix)

matrix = [
    [2,4,6],
    [4,9,14],
    [6,14,23]
]

m1 = Matrix(man=[[2, 4, 6], [1, 5, 9], [3, 7, 8]])  # elimination will involve fractions
m2 = Matrix(man=[[0, 2, 1], [3, 0, 4], [1, 5, 0]])  # zero pivot in first row
m3 = Matrix(man=[[1, 1, 1], [2, 2, 3], [4, 5, 6]])  # near-singular, tricky elimination
m4 = Matrix(man=[[1, 2, 3], [2, 4, 6], [3, 6, 9]])  # determinant is zero (skip?), instead tweak
m5 = Matrix(man=[[0, 1, 2], [1, 0, 3], [4, 5, 6]])  # zero in top-left, requires pivoting

matrices = [m1, m2, m3, m4, m5]
determinants = [12, 27, -3, 1, 3]

def tests(matrices):

    for index, matrix in enumerate(matrices):

        det, res = gaussian(matrix)

        if det == determinants[index]:
            print(f"PASSED {index+1}/{len(matrices)}")
        
tests(matrices)