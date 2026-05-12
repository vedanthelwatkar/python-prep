nums = [5,5,1, 1,9,8,7,8,5, 1, 2, 2, 2, 3, 4, 4]

def k_most_frequent(nums, k):
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1

    hashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
    return [key for key, value in hashmap[:k]]
print("K Most Frequent", k_most_frequent(nums, 2))
