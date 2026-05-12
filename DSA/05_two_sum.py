"""
Two Sum Problem
Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    """
    Find two numbers that add up to the target.
    Returns the indices of the two numbers.
    Uses hashmap for O(n) solution.
    """
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
    return []

# Test cases
print("Two Sum [12, 14, 17, 19] target=26:", two_sum([12, 14, 17, 19], 26))
print("Two Sum [2, 7, 11, 15] target=9:", two_sum([2, 7, 11, 15], 9))
print("Two Sum [3, 3] target=6:", two_sum([3, 3], 6))
