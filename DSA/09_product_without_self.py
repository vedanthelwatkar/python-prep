nums = [1, 2, 3, 4]

def product_without_self(nums, target):
    n = len(nums)
    product = 1

    for i in range(n):
        product =  product * nums[i] if nums[i] != target else product

    return product

print("Product Without Self:", product_without_self(nums, 2))


def productExceptSelf(nums):
    res = [1] * len(nums)

    for left in range(len(nums)):
       for right in range(len(nums)):
           if right != left:
               res[left] *= nums[right]
    return res

print("Product Except Self:", productExceptSelf(nums))