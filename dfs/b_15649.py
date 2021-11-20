n, m = map(int, input().split())
v = [False] * (n + 1)

def dfs(s):
    if len(s) == m:
        print(' '.join(s))
        return

    for i in range(1, n + 1):
        if not v[i]:
            v[i] = True
            dfs(s + [str(i)])
            # s.append(str(i))
            # dfs(s)
            # s.pop()
            v[i] = False # backtracking

dfs([])