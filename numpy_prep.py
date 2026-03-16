import numpy as np

print("ways to create np arr ==> ")
np.array([4,5,6])
np.zeros(5) # array with 5 zeros
np.ones(6) # array with 6 ones

arr = np.arange(1,21) # most asked and used

print('common operations ==> ')
arr + 5 # elements plus 5
arr * 5 # elements multiply by 5
arr - 5 # elements minus 5
arr % 5 == 0 # divide by 5 remainder 0
print(arr.mean())
print(arr.sum())
print(arr.max())
print(arr.min())

print("indexing techniques ==>")
print(arr[1:5]) # 1 to 5
print(arr[5:10:2]) # 5 to 10 with step 2 
print(arr[::-1]) # reverse

mat = np.array([arr, np.arange(20,40)])
print(mat)
print(mat[0,2]) # multidimensional indexing

print(mat.shape) # get the shape of arr
print(mat.reshape(8,5)) # reshape in diff types
