# 5
# 0
# 2 3 2
# 0
# 0
# 0

import heapq

n = int(input())

q = []
ans = []
for _ in range(n):
    nums = input()
    if nums == '0':
        if q:
            print(-heapq.heappop(q))
        else:
            print(-1)
    else:
        l = list(map(int, nums.split()))
        for i in range(1, l[0] + 1):
            heapq.heappush(q, -int(l[i]))