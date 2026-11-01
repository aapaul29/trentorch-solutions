import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    m = np.max(np.abs(x))
    if m == 0.0:
        raise ValueError
    y = x / m                          # entries in [-1, 1], no overflow possible
    return y / np.sqrt(np.dot(y, y))
