"""
Selection Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
"""

lst = [1, 4, 3, 8, 6, 4, 4, 6, 0, 7, 4, 2, 2, 9, 4, 3, 2, 6]

def sorter(nums):
    """
    Selection sort implementation.
    Finds the smallest element and places it at the beginning.
    """
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print("Selection Sort Result:", sorter(lst))
