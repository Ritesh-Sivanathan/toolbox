# Still in development

def gaussian(matrix):

    for z in range(len(matrix)):

        for row in range(z+1, len(matrix)):
            
            if matrix[row][z] != 0:

                f = matrix[row][z] / matrix[z][z]

                for nin, element in enumerate(matrix[row]):
                    matrix[row][nin] -= matrix[row-1][z]*f

    d = 0

    for i in range(len(matrix)):
        # print(matrix[i][i])
        # print(i,i)
        d *= matrix[i][i]

    print(matrix)

matrix = [
    [2,4,6],
    [4,9,14],
    [6,14,23]
]

gaussian(matrix)