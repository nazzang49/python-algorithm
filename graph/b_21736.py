from collections import deque

def bfs(i, j):
    global cnt
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 'O':
                    maps[nx][ny] = 'X'
                    q.append((nx, ny))
                    continue
                if maps[nx][ny] == 'P':
                    cnt += 1
                    maps[nx][ny] = 'X'
                    q.append((nx, ny))


n, m = map(int, input().split())
maps = [[s for s in input()] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            bfs(i, j)
            if cnt > 0:
                print(cnt)
            else:
                print('TT')
            cnt = 0