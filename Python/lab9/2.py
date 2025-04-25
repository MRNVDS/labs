import numpy as np

def run_length_encoding(x: np.ndarray):
    if x.size == 0:
        return np.array([], dtype=x.dtype), np.array([], dtype=int)
    mask = np.concatenate(([True], x[1:] != x[:-1]))
    values = x[mask]
    idx = np.where(mask)[0]
    idx = np.concatenate((idx, [x.size]))
    counts = np.diff(idx)
    return values, counts

x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = run_length_encoding(x)
print("Values:", values)
print("Counts:", counts) 
