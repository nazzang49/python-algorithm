# https://www.acmicpc.net/problem/2110

n, k = map(int, input().split())
pos = [int(input()) for _ in range(n)]

# sort
pos.sort()

# parametric search
left = 1
right = pos[-1] - pos[0]
ans = 0
while left <= right:
    mid = (left + right) // 2 # 인접 최대 거리
    current = pos[0]
    cnt = 1
    
    for i in range(1, len(pos)):
        if pos[i] >= current + mid:
            cnt += 1
            current = pos[i]

    if cnt >= k:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
