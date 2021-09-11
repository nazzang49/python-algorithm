from collections import deque

maps = [[s for s in input()] for _ in range(10)]
v = [[False for _ in range(10)] for _ in range(10)]
ans_cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    v[i][j] = True
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 10 and 0 <= ny < 10:
                if maps[nx][ny] == 'O' and not v[nx][ny]:
                    v[nx][ny] = True
                    q.append((nx, ny))

for i in range(10):
    for j in range(10):
        if maps[i][j] == 'O' and not v[i][j]:
            ans_cnt += 1
            bfs(i, j)

if ans_cnt == 0:
    print(-1)
else:
    print(ans_cnt)