import numpy as np
matrix_text = """3,4,17,-3
5,11,-1,6
0,2,-5,8"""

with open('matrix.txt', 'w') as f:
    f.write(matrix_text)

matrix = np.loadtxt('matrix.txt', delimiter=',')

total_sum = matrix.sum()
max_element = matrix.max()
min_element = matrix.min()

print(f"Matrix:\n{matrix}")
print(f"Sum of all elements: {total_sum}")
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")
