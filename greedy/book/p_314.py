n = int(input())
n_list = [int(s) for s in input().split()]
n_list.sort()

target = 1
for i in n_list:
    if target < i:
        break
    target += i
print(target)