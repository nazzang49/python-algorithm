nums = [1,2,3]
v = [False] * len(nums)
ans = []
def dfs(num_list):
    if len(nums) == len(num_list):
        ans.append(num_list)
        return

    for i in range(len(nums)):
        if not v[i]:
            v[i] = True
            dfs(num_list + [nums[i]]) # append is impossible unless using copy (e.g) num_list.copy()
            v[i] = False

dfs([])
print(ans)

# itertools
from itertools import combinations, permutations
print(list(map(list, permutations(nums)))) # tuple to list

# combinations => nCr
for c in combinations(nums, 2):
    print(c)