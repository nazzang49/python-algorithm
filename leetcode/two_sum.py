nums = [2,7,11,15]
target = 9

# bruteforce
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

# dict
d = dict()
for i, n in enumerate(nums):
    d[n] = i

for i, n in enumerate(nums):
    if target - n in d and i != d[target - n]: # in comparing is possible on key-level
        print([i, d[target - n]])
