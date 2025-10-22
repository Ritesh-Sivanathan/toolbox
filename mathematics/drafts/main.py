from ..linear_algebra.matrices import Matrix

def gaussian(matrix):

    det = 1
    
    row_swap = False
    found = False

    if isinstance(matrix, Matrix):
        matrix = matrix.matrix

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

matrix = [
    [2,4,6],
    [4,9,14],
    [6,14,23]
]

m1 = Matrix(man=[[2, 1, 3], [1, 4, 2], [3, 2, 1]])   # standard case
m2 = Matrix(man=[[0, 2, 1], [1, 3, 4], [2, 1, 5]])   # zero pivot in first position
m3 = Matrix(man=[[1, 2, 3], [2, 4, 6], [1, 1, 1]])   # singular - row 2 = 2*row 1
m4 = Matrix(man=[[3, 0, 0], [0, 2, 0], [0, 0, 4]])   # diagonal matrix
m5 = Matrix(man=[[1, -1, 2], [2, 3, 1], [-1, 2, 3]]) # with negative values

matrices: list[Matrix] = [m1, m2, m3, m4, m5]
determinants = [-25, 1, 0, 24, 28]

def tests(matrices):

    for index, matrix in enumerate(matrices):

        try:

            det, res = gaussian(matrix)

            if det == determinants[index]:
                print(f"PASSED {index+1}/{len(matrices)}")

            print(det,res,determinants[index])

            if index == 5:
                print(det, res)
        
        except err as err:
            print(err)

def comparison_tests(matrices):

    for index, matrix in enumerate(matrices):

        try:

            if matrix.det() == determinants[index]:
                print(f"TEST {index+1}/{len(matrices)} PASSED")
        
        except err as err:
            print(err)

comparison_tests(matrices)