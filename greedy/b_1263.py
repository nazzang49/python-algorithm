n = int(input())

arr = []
for i in range(n):
    t, s = map(int, input().split())
    arr.append((t, s))

arr = sorted(arr, key=lambda x: x[1], reverse=True)

max_start = arr[0][1] - arr[0][0]
for i in range(1, n):
    if max_start > arr[i][1]:
        max_start = arr[i][1] - arr[i][0]
    else:
        max_start -= arr[i][0]

print(max_start if max_start >=0 else -1)


# 4
# 3 5
# 8 14
# 5 20
# 1 16