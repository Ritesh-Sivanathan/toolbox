from mathematics.linear_algebra.matrices import Matrix

import matplotlib.pyplot as plt
import random

# import numpy as np

def Sierpinski_Triangle(bounds=[-100,100], s=1/2, iter=20):
    
    # corners of the triangle; can change these to alter shape
    
	c_top = Matrix(man=[[0.5], [0]]) 
	c_left = Matrix(man=[[0], [0]])
	c_right = Matrix(man=[[0], [0.5]])

	points = []

	for x in range(bounds[0], bounds[1]): # replace with np.arange and a floating-point increment for intricate details
		for y in range(bounds[0], bounds[1]): # replace with np.arange and a floating-point increment for intricate details
	
			v_curr = Matrix(man=[[(x-bounds[0])/(bounds[1] - bounds[0])], [(y-bounds[0])/(bounds[1] - bounds[0])]]) # normalizing the x and y points to match large bounds
   	
			for _ in range(iter): # iterations
		
				choice = random.choice([c_top, c_left, c_right])
		
				v_new = (s) * v_curr + choice
	
				v_curr = v_new

			# TODO: can this flattening be more efficient?		
  
			points.append([item for row in v_curr.matrix for item in row]) # flattens the list.
   
	return points

data = Sierpinski_Triangle(bounds=[-100,100])

x_coords = [p[0] for p in data]
y_coords = [p[1] for p in data]

plt.scatter(x_coords, y_coords, s=0.1)
plt.show()
