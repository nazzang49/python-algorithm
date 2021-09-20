from collections import deque

a, b, c = map(int, input().split())
v = [[False] * 1501 for _ in range(1501)]

def bfs(total):
    global a, b, c
    q = deque()
    q.append((a, b))
    v[a][b] = True

    while q:
        a, b = q.popleft()
        c = total - (a + b)
        if a == b == c:
            print(1)
            exit()
        for j, k in ((a, b), (a, c), (b, c)):
            if j > k:
                j -= k
                k += k
            elif k > j:
                k -= j
                j += j
            else:
                continue # 같으면 더 이상 연산 불가
            l = total - (j + k)
            j = min(min(j, k), l)
            k = max(max(j, k), l)
            if not v[j][k]:
                q.append((j, k))
                v[j][k] = True
    print(0)

# 합산 결과가 3으로 나눠지지 않으면 무조건 불가능
total = a + b + c
if total % 3 != 0:
    print(0)
else:
    bfs(total)