from collections import deque

n, k = map(int, input().split())
n += 1

v = [False] * n
maps = [[] * k for _ in range(n)]
ans = []
for i in range(1, n):
    maps[i] = [s for s in input()]

def is_hamming(a_list, b_list):
    cnt = 0
    for i in range(len(a_list)):
        if a_list[i] != b_list[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

# 간선 연결
line = [[False] * n for _ in range(n)]
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if is_hamming(maps[i], maps[j]):
            line[i][j] = line[j][i] = True

def bfs(s, e):
    q = deque()
    q.append(s)
    now = 0
    v[s] = True
    way = [0 for _ in range(n)]

    while q:
        now = q.popleft()
        if now == e:
            break

        for i in range(1, n):
            if not v[i] and line[now][i]:
                v[i] = True
                q.append(i)
                # 현위치 값 => 이전 위치 인덱스 (경로 확인)
                way[i] = now

    if now != e:
        print(-1)
    else:
        # 뒤에서부터 경로 확인
        ans.append(e)
        j = 0
        while True:
            idx = ans[j]
            if idx == s:
                break
            ans.append(way[idx])
            j += 1

    final_ans = ''
    for i in range(len(ans) - 1, -1, -1):
        final_ans = final_ans + str(ans[i]) + ' '
    print(final_ans)

s, e = map(int, input().split())
bfs(s, e)