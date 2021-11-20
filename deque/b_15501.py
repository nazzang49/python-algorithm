from collections import deque

n = int(input())
p = [int(s) for s in input().split()]
permutation1 = deque(p)
permutation2 = deque(p[::-1])
answer = deque([int(s) for s in input().split()])

for _ in range(n):
    permutation1.append(permutation1.popleft())
    permutation2.append(permutation2.popleft())

    if permutation1 == answer or permutation2 == answer:
        print('good puzzle')
        exit()

print('bad puzzle')