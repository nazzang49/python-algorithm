# 5 4
# 1 3
# 4 2
# 2 5
# 3 2
import sys
from itertools import combinations

inf = sys.maxsize
n, m = list(map(int, input().split()))

lines = []
for i in range(m):
    a, b = list(map(int, input().split()))
    lines.append((a, b))

cost = [[inf] * (n + 1) for _ in range(n + 1)]
for line in lines:
    cost[line[0]][line[1]] = cost[line[1]][line[0]] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # if k == x or k == y: # chicken
            if cost[j][k] > cost[j][i] + cost[i][k]:
                cost[j][k] = cost[j][i] + cost[i][k]

ans = []
for c in combinations(range(1, n + 1), 2):
    time = 0
    for i in range(1, n + 1):
        if i == c[0] or i == c[1]:
            continue
        if cost[i][c[0]] < cost[i][c[1]]:
            time += cost[i][c[0]] * 2
        else:
            time += cost[i][c[1]] * 2
    ans.append((c[0], c[1], time))

ans = sorted(ans, key=lambda x: (x[2], x[0], x[1]))
print(ans[0][0], ans[0][1], ans[0][2], end=' ')