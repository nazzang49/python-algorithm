from itertools import combinations

def check_up(r, c):
    while r >= 0:
        if map[r][c] == 'S':
            return False
        if map[r][c] == 'O':
            return True
        r -= 1
    return True

def check_down(r, c):
    while r < n:
        if map[r][c] == 'S':
            return False
        if map[r][c] == 'O':
            return True
        r += 1
    return True

def check_left(r, c):
    while c >= 0:
        if map[r][c] == 'S':
            return False
        if map[r][c] == 'O':
            return True
        c -= 1
    return True

def check_right(r, c):
    while c < n:
        if map[r][c] == 'S':
            return False
        if map[r][c] == 'O':
            return True
        c += 1
    return True

# check up / down / left / right
def is_ok():
    for t in teacher:
        r, c = t
        if not check_up(r, c): return False
        if not check_down(r, c): return False
        if not check_left(r, c): return False
        if not check_right(r, c): return False
    return True

n = int(input())
map = [input().split() for _ in range(n)]
teacher = []
safe = []
for i, r in enumerate(map):
    for j, c in enumerate(r):
        if c == 'X':
            safe.append((i, j))
        elif c == 'T':
            teacher.append((i, j))

flag = False
for obstacles in combinations(safe, 3):
    for obstacle in obstacles:
        r, c = obstacle
        map[r][c] = 'O'
    if is_ok():
        print('YES')
        flag = True
        break
    for obstacle in obstacles:
        r, c = obstacle
        map[r][c] = 'X'
if not flag:
    print('NO')