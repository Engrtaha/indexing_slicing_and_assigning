import numpy as np
example = np.arange(1,17).reshape(4,4)
print("Original Array:")
print(example)
print("Accessing specific elements using fancy indexing:")
print(example[1,[1,3]])
print(example[[0,3],1])