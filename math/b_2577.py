n = 1
for i in range(3):
    n *= int(input())

n_str = str(n)
for i in range(10):
    print(f'{n_str.count(str(i))}')