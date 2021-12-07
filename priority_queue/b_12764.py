# 5
# 20 50
# 10 100
# 30 120
# 60 110
# 80 90

import heapq

n = int(input())
q = []
ans = []
for _ in range(n):
    s, e = list(map(int, input().split()))
    heapq.heappush(q, (s, e))

idx = 0
s, e = heapq.heappop(q)
heapq.heappush(ans, (e, idx, 1))
while q:
    s, e = heapq.heappop(q)
    tmp_e, tmp_idx, tmp_p = heapq.heappop(ans)

    if s >= tmp_e:
        heapq.heappush(ans, (e, tmp_idx, tmp_p + 1))
    else:
        heapq.heappush(ans, (tmp_e, tmp_idx, tmp_p))
        idx += 1
        heapq.heappush(ans, (e, idx, 1))

print(len(ans))
ans = sorted(ans, key=lambda x: x[1])
for a in ans:
    print(a[2], end=' ')