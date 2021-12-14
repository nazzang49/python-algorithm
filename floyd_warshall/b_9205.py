import sys

inf = sys.maxsize

def floyd(L):
    c = [[inf] * len(L) for _ in range(len(L))]

    for i in range(len(L)):
        for j in range(len(L)):
            if i == j:
                continue
            if abs(L[i][1] - L[j][1]) + abs(L[i][0] - L[j][0]) <= 1000:
                c[i][j] = 1

    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                if c[j][k] > c[j][i] + c[i][k]:
                    c[j][k] = c[j][i] + c[i][k]

    print('happy' if c[0][len(L) - 1] < inf else 'sad')

t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    location = [(x, y)]

    for _ in range(n):
        x, y = map(int, input().split())
        location.append((x, y))

    x, y = map(int, input().split())
    location.append((x, y))
    floyd(location)