import numpy as np
data = np.random.randn(10, 4)

min_val = data.min()
max_val = data.max()
mean_val = data.mean()
std_val = data.std()

first_five_rows = data[:5, :]

print("Data (10x4):\n", data)
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Mean: {mean_val}")
print(f"Standard Deviation: {std_val}")
print("First 5 rows:\n", first_five_rows)
