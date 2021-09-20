def dfs(s, e, ans):
    global flag
    if s == e:
        flag = True
        print(ans)
        return
    for i in range(1, n):
        if not v[i] and line[s][i]:
            v[i] = True
            dfs(i, e, ans + ' ' + str(i))

# 해밍 경로 (해밍 거리 = 1) 확인
def is_hamming(a_list, b_list):
    cnt = 0
    for i in range(k):
        if a_list[i] != b_list[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False

# 해밍 거리 간선 연결
def connect_line():
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if is_hamming(maps[i], maps[j]):
                line[i][j] = line[j][i] = True

n, k = map(int, input().split())
n += 1

v = [False] * n
maps = [[] * k for _ in range(n)]
for i in range(1, n):
    maps[i] = [s for s in input()]

line = [[False] * n for _ in range(n)]
connect_line()

s, e = map(int, input().split())
v[s] = True
flag = False

dfs(s, e, str(s))
if not flag:
    print(-1)


# 5 3
# 000
# 111
# 001
# 010
# 110
# 1 2