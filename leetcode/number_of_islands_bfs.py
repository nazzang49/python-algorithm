from collections import deque

maps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        pos = q.popleft()
        cur_r = pos[0]
        cur_c = pos[1]

        for i in range(4):
            nr = cur_r + maps[i][0]
            nc = cur_c + maps[i][1]

            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue

            if grid[nr][nc] == '1':
                grid[nr][nc] = '0'
                q.append((nr, nc))

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1':
            ans += 1
            bfs(i, j)

print(ans)