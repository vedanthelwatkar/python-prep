"""
Bubble Sort Algorithm
Time Complexity: O(n²)
Space Complexity: O(1)
"""

lst = [1, 4, 3, 8, 6, 4, 4, 6, 0, 7, 4, 2, 2, 9, 4, 3, 2, 6]

def bubble_sort(nums):
    """
    Bubble sort implementation.
    Compares adjacent elements and swaps if they're in wrong order.
    """
    n = len(nums)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print("Bubble Sort Result:", bubble_sort(lst))
