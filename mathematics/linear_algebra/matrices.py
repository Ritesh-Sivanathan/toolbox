# define matrix class
# can be used to create an nxk matrix
# should have a description function to give details on matrix in a concise format

class Matrix:

    def __init__(self, r:int, c:int, mode:str='zero', fill:int=0):

        '''

        `Matrix` object of `r*c` dimensions, where `r` is the number of rows and `c` is the number of columns.

        ### Required Arguments
        
        `r`: Number of **rows** in the Matrix \\
        `c`: Number of **columns** in the Matrix
        
        ### Optional arguments:

        `mode` *(default="zero")*: Populate all elements of the Matrix with: zeroes ("zero"), empty ("empty"), fill ("fill")
        `fill` *(default=0)*: If using `mode="fill"`, populates Matrix with real number `fill`
        
        '''
        
        if mode not in {"zero", "empty", "fill"}:
            raise ValueError(f"Unsupported mode '{mode}'. Use 'zero', 'empty' or 'fill'.")

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

    def __repr__(self):
        return f'Matrix({self.r}, {self.c}, "{self.mode}")'

    def show(self):

        '''
        
        Returns string in this format:
            `rows x cols`
        
        '''

        return f"{self.r}x{self.c}"
    
    def det(self):

        '''
        
        ### Only supported for 2x2 matrices for now
        Returns the single value for the determinant of the `Matrix`
        
        '''

        if self.r != 2 or self.c != 2:
            raise ValueError("Determinant only defined for 2x2 matrices")
        
        det = (self.matrix[0][0]*self.matrix[1][1]) - (self.matrix[0][1]*self.matrix[1][0])

        return det