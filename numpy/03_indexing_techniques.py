"""
NumPy: Indexing Techniques
Slicing and indexing in NumPy arrays (1D and 2D)
"""

import numpy as np

arr = np.arange(1, 21)
mat = np.array([arr, np.arange(20, 40)])

print("=" * 50)
print("NumPy Indexing Techniques")
print("=" * 50)

print("\n1D Array Indexing:")
print("arr[1:5] =", arr[1:5])
print("arr[5:10:2] =", arr[5:10:2])
print("arr[::-1] (reversed) =", arr[::-1])

print("\n2D Array (Matrix):")
print("Matrix:")
print(mat)

print("\nMultidimensional Indexing:")
print("mat[0, 2] =", mat[0, 2])

print("\nMatrix Shape and Reshape:")
print("mat.shape =", mat.shape)
print("mat.reshape(8, 5) =")
print(mat.reshape(8, 5))
