import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

preceded_by_zero = x[np.where(np.concatenate(([False], x[:-1] == 0)))]
max_value = preceded_by_zero.max() if preceded_by_zero.size > 0 else None

print(f"Original array: {x}")
print(f"Elements preceded by zero: {preceded_by_zero}")
print(f"Maximum among them: {max_value}")
