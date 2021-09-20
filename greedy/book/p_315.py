from itertools import combinations

n, m = map(int, input().split())
bowling = list(map(int, input().split()))

cnt = 0
for cb in combinations(bowling, 2):
    l, r = cb
    if l != r:
        cnt += 1
print(cnt)