import numpy as np
array = np.arange(30).reshape(6,5)
print("it's a 2D original array")
print(array)
print("it will print all rows and columns from index 0 to 4 with step 2")
print(array[0::2, 0::2])
