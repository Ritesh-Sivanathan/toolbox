

class Vector:

    def __init__(self, vector: list):

        if not isinstance(vector, list):
            raise TypeError("Vectors must be defined using a valid list")

        self.vector = vector
        self.dims = len(vector)

    def __add__(self, vector):
        
        vector_sum = [0, 0, 0]

        vector = self.__preprocess_(vector)

        for index in range(len(self.vector)):
            vector_sum[index] = self.vector[index] + vector.vector[index]
        
        return Vector(vector_sum)

    def __sub__(self, vector):
        
        vector_diff = [0, 0, 0]

        vector = self.__preprocess_(vector)

        for index in range(len(self.vector)):
            vector_diff[index] = self.vector[index] - vector.vector[index]
        
        return Vector(vector_diff)
    
    def __mul__(self, vector):

        """
        
        Dot product of two vectors
        
        """

        pass

    @staticmethod
    def __preprocess_(vector):

        if isinstance(vector, list[int]):

            vector = Vector(vector)
        
        if not isinstance(vector, Vector):

            raise TypeError("Please provide a valid vector")
