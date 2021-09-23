from collections import deque

n, k = map(int, input().split())
maps = [[int(s) for s in input().split()] for _ in range(n)]

# 8개 방향
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(x, y):
    q = deque()
    maps[x][y] = 0
    q.append((x, y))

    while q:
        r, c = q.popleft()
        for i in range(8):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0 <= nx < n and 0 <= ny < k:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    q.append((nx, ny))

cnt = 0
for i in range(n):
    for j in range(k):
        if maps[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)


# 8 19
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0
# 0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0
# 0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0
# 0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0 0 0
# 0 1 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0
# 0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0