grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
ans = 0

def dfs(i, j):
  if grid[i][j] != '1' or i < 0 or j >= len(grid[0]):
    return # pruning => no more 1 (land) or out of index
  grid[i][j] = '0' # visit 1 (land)

  # go to each directions
  dfs(i - 1, j)
  dfs(i + 1, j)
  dfs(i, j - 1)
  dfs(i, j + 1)

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == '1': # connected but not visited yet
      ans += 1
      dfs(i, j)

print(ans)
