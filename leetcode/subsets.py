nums = [1,2,3]
ans = []

def dfs(s, subsets):
    ans.append(subsets)
    for i in range(s, len(nums)):
        dfs(i + 1, subsets + [nums[i]]) # better use list summation than append function in DFS

dfs(0, [])
print(ans)