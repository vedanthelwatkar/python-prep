nums = [0, 1, 0, 3, 12]

def shift_zero_end(nums):
    res = [0] * len(nums)
    ind = 0
    for num in nums:
        if num !=0:
            res[ind] = num
            ind += 1
    return res

print("Shift Zero to End:", shift_zero_end(nums))