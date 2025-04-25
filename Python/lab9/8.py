import numpy as np

arr = np.array([0,1,2,0,0,4,0,6,9])
indices = np.nonzero(arr)[0]

print("Array:", arr)
print("Indices of non-zero elements:", indices)
