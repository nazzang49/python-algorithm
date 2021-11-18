# https://www.acmicpc.net/problem/14713

from collections import deque

n = int(input())
S = []
for _ in range(n):
    S.append(deque(input().split()))
L = input()

def is_possible(w:str):
    for i, q in enumerate(S):
        if q and q[0] == w:
            q.popleft()
            return True
    return False

for w in L.split():
    if not is_possible(w):
        print('Impossible')
        exit()

for q in S:
    if q:
        print('Impossible')
        exit()

print('Possible')