"""
NumPy: Creating Arrays
Different ways to create numpy arrays
"""

import numpy as np

print("=" * 50)
print("Ways to Create NumPy Arrays")
print("=" * 50)

# Method 1: Using np.array()
arr1 = np.array([4, 5, 6])
print("\nUsing np.array():")
print(arr1)

# Method 2: Using np.zeros()
arr2 = np.zeros(5)
print("\nUsing np.zeros(5):")
print(arr2)

# Method 3: Using np.ones()
arr3 = np.ones(6)
print("\nUsing np.ones(6):")
print(arr3)

# Method 4: Using np.arange()
arr4 = np.arange(1, 21)
print("\nUsing np.arange(1, 21):")
print(arr4)
