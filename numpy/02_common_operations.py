"""
NumPy: Common Operations
Arithmetic operations and aggregations on arrays
"""

import numpy as np

arr = np.arange(1, 21)

print("=" * 50)
print("NumPy Common Operations")
print("=" * 50)

print("\nOriginal Array:")
print(arr)

print("\nArithmetic Operations:")
print("arr + 5 =", arr + 5)
print("arr * 5 =", arr * 5)
print("arr - 5 =", arr - 5)

print("\nModulo Operation:")
print("arr % 5 == 0 =", arr % 5 == 0)

print("\nAggregation Functions:")
print("arr.mean() =", arr.mean())
print("arr.sum() =", arr.sum())
print("arr.max() =", arr.max())
print("arr.min() =", arr.min())
