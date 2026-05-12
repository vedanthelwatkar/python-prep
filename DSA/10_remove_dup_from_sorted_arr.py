arr = [1, 1, 2, 2, 3, 3]

def remove_duplicates(arr):
    if not arr:
        return 0

    res = []
    for num in arr:
        if num not in res:
            res.append(num)
    return res


print("Remove Duplicates:", remove_duplicates(arr))

# solve this using two pointer approach later