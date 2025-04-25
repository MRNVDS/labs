import numpy as np
from numpy.linalg import det, inv
from scipy.stats import multivariate_normal
import time

def logpdf_manual(X, m, C):
    X = np.atleast_2d(X)
    m = m.reshape(-1)
    d = m.size
    C_inv = inv(C)
    C_det = det(C)
    norm_const = -0.5 * (d * np.log(2 * np.pi) + np.log(C_det))
    diffs = X - m
    exponent = -0.5 * np.sum(diffs @ C_inv * diffs, axis=1)
    return norm_const + exponent

D = 3
m = np.zeros(D)
C = np.eye(D)
X = np.random.randn(1000, D)

manual = logpdf_manual(X, m, C)
scipy_vals = multivariate_normal(mean=m, cov=C).logpdf(X)
print("Max absolute difference:", np.max(np.abs(manual - scipy_vals)))

start = time.time()
logpdf_manual(X, m, C)
print("Manual time:", time.time() - start)

start = time.time()
multivariate_normal(mean=m, cov=C).logpdf(X)
print("SciPy time:", time.time() - start)
