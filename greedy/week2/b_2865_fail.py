from itertools import combinations

tmp_list = input().split()

n = int(tmp_list[0])
m = int(tmp_list[1])
k = int(tmp_list[2])

def get_pairs(s: str):
    s_list = s.split()
    pairs = []
    for i in range(0, len(s_list) - 1, 2):
        pairs.append((int(s_list[i]), float(s_list[i + 1])))
    return pairs

scores = dict()
pairs = []
for i in range(m):
    s = input()
    pairs += get_pairs(s)

def is_duplicate(cbs):
    n_list = [p for (p, v) in cbs]
    for n in n_list:
        if n_list.count(n) >= 2:
            return False
    return True

def calc_sum(cbs):
    total = 0
    for (p, v) in cbs:
        total += v
    return total

ans = 0
for cbs in combinations(pairs, k):
    if is_duplicate(cbs):
        ans = max(ans, calc_sum(cbs))

print(ans)

