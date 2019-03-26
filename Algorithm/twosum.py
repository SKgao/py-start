def towSum(nums, target):
    t = {}
    for i, n in enumerate(nums):
        if n in t:
            return [t[n], i]
        t[target - n] = i
    return []
print(towSum([2, 7, 5, 10], 9))