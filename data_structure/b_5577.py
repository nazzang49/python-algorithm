n = int(input())
n_list = []
for i in range(n):
    n_list.insert(0, int(input()))
rem = 0

def calc(i, j):
    front = i
    back = i
    n_list[i] = j # 현재 지점 색 변경
    total = 0
    while front >= 0 and back < n and n_list[front] == n_list[back]:
        c_tmp = n_list[front]
        cnt = 0

        # 왼쪽 동일 색 여부 확인
        while front >= 0 and n_list[front] == c_tmp:
            cnt += 1
            front -= 1

        # 오른쪽 동일 색 여부 확인
        while back < n and n_list[back] == c_tmp:
            cnt += 1
            back += 1

        if cnt >= 4:
            total += cnt

    return total

for i in range(n):
    for j in range(1, 4):
        c_origin = n_list[i] # 기존
        rem = max(rem, calc(i, j) - 1)
        n_list[i] = c_origin # 원복

print(n - rem)