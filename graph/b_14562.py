def dfs(cnt, s, t):
    global ans
    if s == t:
        ans = min(ans, cnt)
        return

    if s > t:
        return

    dfs(cnt + 1, s * 2, t + 3)
    dfs(cnt + 1, s + 1, t)

n = int(input())
scores = []
ans = float('inf')
for i in range(n):
    s, t = map(int, input().split())
    dfs(0, s, t)
    print(ans)
    ans = float('inf')
