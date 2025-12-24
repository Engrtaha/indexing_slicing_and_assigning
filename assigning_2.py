import numpy as np
x = np.arange(9).reshape(3,3)
x[1,1]=100 # assign value to the mid of the array 
x[:,2]=100 #slicing two 2D array and assigning values

print(x)