import copy

nums = [1,2,3]
v = [False] * len(nums)
ans = []
def dfs(num_list):
    if len(nums) == len(num_list):
        tmp_list = copy.deepcopy(num_list) # caution
        ans.append(tmp_list)
        return

    for i in range(len(nums)):
        if not v[i]:
            v[i] = True
            num_list.append(nums[i])
            dfs(num_list)
            num_list.pop()
            v[i] = False

dfs([])
print(ans)

# itertools
from itertools import combinations, permutations
print(list(map(list, permutations(nums)))) # tuple to list

# combinations => nCr
for c in combinations(nums, 2):
    print(c)