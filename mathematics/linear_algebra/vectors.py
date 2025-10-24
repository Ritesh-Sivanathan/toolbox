from ..linear_algebra.matrices import Matrix

class Vector:

    def __init__(self, vector: list):

        if not isinstance(vector, list):
            raise TypeError("Vectors must be defined using a valid list")

        self.vector = vector
        self.dims = len(vector)

    def __add__(self, vector):
        
        vector_sum = [0, 0, 0]

        vector = self.__preprocess__(vector, same_size=True)

        for index in range(len(self.vector)):
            vector_sum[index] = self.vector[index] + vector.vector[index]
        
        return Vector(vector_sum)

    def __sub__(self, vector):
        
        vector_diff = [0, 0, 0]

        vector = self.__preprocess__(vector, same_size=True)

        for index in range(len(self.vector)):
            vector_diff[index] = self.vector[index] - vector.vector[index]
        
        return Vector(vector_diff)
    
    def __mul__(self, multiple):

        """
        
        Dot product of two vectors (if )
        
        """

        if isinstance(multiple, (Vector, list)):

            vector = multiple
            
            vector = self.__preprocess__(vector, same_size=True)

            dot_product = 0

            for index in range(len(vector.vector)):
                dot_product += self.vector[index] * vector.vector[index]

            return dot_product
    
    def n_dimensional_vector(self, n:int):

        """
        
        Returns an n-dimensional vector filled with zeroes
            [will add more options for fill values later]

        """

        if not isinstance(n, int):
            return TypeError("n must be a valid integer")

        vector = [0 for _ in range(n)]

        return vector
    
    def cross_product(self, vector):
        
        """
        
        Cross product of two vectors in 3-space

        """

        vector = self.__preprocess__(self, vector)
        
        dimensions = len(vector.vector)

        i = [1,0,0]
        j = [0,1,0]
        k = [0,0,1]

        unit_vectors = [i,j,k]

        dot_product = Vector([0,0,0])

        for row in range(1, dimensions):
            
            new_matrix = [self.vector, vector.vector]
            
            for element in range(1, dimensions):

                del new_matrix[row][element]
                matrix = new_matrix
                det, _ = Matrix(man=matrix).gaussian_elimination()
                
                dot_product += det * unit_vectors[element]

        print(dot_product)
        
    def __preprocess__(self, vector, same_size=False):

        if isinstance(vector, list) and all(isinstance(element, int) for element in vector):

            vector = Vector(vector)

            if same_size and len(vector.vector) != len(self.vector):
                print(len(vector.vector), len(self.vector))
                raise ValueError("Vectors must be of the same size to perform this operation")
            
            return vector
        
        if not isinstance(vector, (Vector, list)):

            raise TypeError("Please provide a valid vector")
        
        if same_size and len(vector.vector) != len(self.vector):
                raise ValueError("Vectors must be of the same size to perform this operation")

        return vector