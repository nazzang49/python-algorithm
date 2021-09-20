import copy

def dfs(s, e, way: list):
    if s == e:
        new_way = copy.deepcopy(way)
        ans.append(new_way)
        return

    # 해밍경로 (해밍거리 1) 확인
    for i in range(1, n):
        if not v[i] and is_hamming(maps[s], maps[i]):
            v[i] = True
            way.append(i)
            print('way : ', way)
            dfs(i, e, way)
            v[i] = False
            way.pop()

def is_hamming(a_list, b_list):
    cnt = 0
    for i in range(len(a_list)):
        if cnt >= 2:
            return False
        if a_list[i] != b_list[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def print_shortest_way():
    global ans

    if ans[0]:
        ans = sorted(ans, key=len)
        print(' '.join(map(str, ans[0])))
    else:
        print(-1)

n, k = map(int, input().split())
n += 1

v = [False] * n
maps = [[] * k for _ in range(n)]
ans = []
for i in range(1, n):
    maps[i] = [s for s in input()]

s, e = map(int, input().split())
way = [s]
v[s] = True

dfs(s, e, way)
print_shortest_way()

