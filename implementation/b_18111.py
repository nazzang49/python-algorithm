# 3 4 99
# 0 0 0 0
# 0 0 0 0
# 0 0 0 1
import sys

n, m, b = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.extend(map(int, input().split()))

# 오름차순 정렬
arr = sorted(arr, reverse=False)

ans = sys.maxsize
h = 0
for i in range(257):
    time = 0
    new_b = b

    for e in arr:
        if i >= e:
            time += (i - e)
            new_b -= (i - e)
        else:
            time += (e - i) * 2
            new_b += (e - i)

    if new_b >= 0 and time <= ans:
        ans = time
        h = i

print(ans, h)