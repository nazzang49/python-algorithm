# 3 4 99
# 0 0 0 0
# 0 0 0 0
# 0 0 0 1

n, m, b = map(int, input().split())

arr = []
for _ in range(n):
    arr.extend(map(int, input().split()))

# 오름차순 정렬
arr = sorted(arr, reverse=False)
answer = []

def is_ok(h, b, arr):
    global answer

    time = 0

    for e in arr:
        if e < h:
            time += (h - e)
            b -= (h - e)
        else:
            time += (e - h) * 2
            b += (e - h)

    # 정답 후보
    if b >= 0:
        answer.append([time, h])
        return True

    return False

# 이분탐색
l = min(arr)
r = max(arr)

while l <= r:
    mid = (l + r) // 2

    if is_ok(mid, b, arr):
        l = mid + 1
    else:
        r = mid - 1

print(sorted(answer, key=lambda x: (x[0], -x[1]))[0])




