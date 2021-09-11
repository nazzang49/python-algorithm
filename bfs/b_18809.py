from collections import deque
from itertools import combinations
import copy

a = list(map(int, input().split()))
n = a[0]
m = a[1]
g = a[2]
r = a[3]
garden = [[int(s) for s in input().split()] for _ in range(n)]
ans_cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(garden, zones, gz):
    global ans_cnt

    cnt = 0
    gq = deque()
    rq = deque()

    for z in zones:
        r, c = z
        if (r, c) in gz:
            gq.append((r, c))
            garden[r][c] = 3
        else:
            rq.append((r, c))
            garden[r][c] = 4

    # -- search
    while gq:
        g_temp = set()
        r_temp = set()

        while gq:
            r, c = gq.popleft()
            garden[r][c] = 3
            for i in range(4):
                nx = r + dx[i]
                ny = c + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if garden[nx][ny] == 1 or garden[nx][ny] == 2:
                        g_temp.add((nx, ny))

        while rq:
            r, c = rq.popleft()
            garden[r][c] = 4
            for i in range(4):
                nx = r + dx[i]
                ny = c + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if garden[nx][ny] == 1 or garden[nx][ny] == 2:
                        r_temp.add((nx, ny))

        # -- common and diff
        intersection = g_temp & r_temp
        g_temp = g_temp - intersection
        r_temp = r_temp - intersection

        for r, c in intersection:
            garden[r][c] = 5
            cnt += 1
        for r, c in g_temp:
            garden[r][c] = 3
        for r, c in r_temp:
            garden[r][c] = 4

        gq.extend(g_temp)
        rq.extend(r_temp)

    ans_cnt = max(ans_cnt, cnt)

zone_list = []
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            zone_list.append((i, j))

for zones in combinations(zone_list, g + r):
    for gz in combinations(zones, g):
        copied_garden = copy.deepcopy(garden)
        bfs(copied_garden, zones, gz)

print(ans_cnt)