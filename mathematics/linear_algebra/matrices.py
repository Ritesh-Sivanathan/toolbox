# define matrix class
# can be used to create an nxk matrix
# should have a description function to give details on matrix in a concise format

class Matrix:

    def __init__(self, r:int, c:int, zeroes=True, empty=False, rand_float=False, rand_int=False):

        '''

        `Matrix` object of `r*c` dimensions, where `r` is the number of rows and `c` is the number of columns.

        ### Required Arguments
        
        `r`: Number of **rows** in the Matrix \\
        `c`: Number of **columns** in the Matrix
        
        ### Optional arguments:

        `zeroes` *(default)*: Populate all elements of the Matrix with **zeroes** \\
        `empty`: Leave all elements of the Matrix **empty** \\
        `rand_float`: Populate all elements of the Matrix with **random floats** \\
        `rand_int`: Populate all elements of the Matrix with **random integers**
        
        '''

        self.r = r
        self.c = c
        self.matrix = [[0]*c]*r if zeroes else [[]*c]*r if empty else [[0]*c]*r
    
        self.populate = 'z' if zeroes else 'e' if empty else 'ri' if rand_int else 'rf' if rand_float else 'z'

    def show(self):

        '''
        
        Returns string in this format:
            `rows x cols 'populate_type'`
        
        '''

        return f"{self.r}x{self.c} '{self.populate}'"

'''

[
[], []
[], []
]

[[], []], [[], []]


'''