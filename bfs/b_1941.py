p = [[s for s in input()] for _ in range(5)]
v = [[False for _ in range(5)] for _ in range(5)]

def check_case(r, c):
    global p, v
    cnt = 0
    cnt += is_same_row(r)
    cnt += is_same_col(c)
    v = [[False for _ in range(5)] for _ in range(5)]
    if cnt >= 4: return True
    return False

def is_same_row(r):
    global p, v
    cnt = 0
    for c in range(5):
        if p[r][c] == 'S':
            v[r][c] = True
            cnt += 1
    return cnt

def is_same_col(c):
    global p, v
    cnt = 0
    for r in range(5):
        if p[r][c] == 'S' and not v[r][c]:
            cnt += 1
    return cnt

ans_cnt = 0
for i in range(5):
    for j in range(5):
        if check_case(i, j):
            ans_cnt += 1
print(ans_cnt)