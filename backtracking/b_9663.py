n = int(input()) # n x n

ans = 0
def is_possible(chess, i):
    for j in range(len(chess)):
        if chess[j] == i or chess[j] == i + (len(chess) - j) or chess[j] == i - (len(chess) - j):
            return False
    return True

def dfs(chess):
    global ans

    if len(chess) == n:
        ans += 1
        return

    for i in range(n):
        if is_possible(chess, i):
            dfs(chess + [i])

for i in range(n):
    dfs([i])

print(ans)