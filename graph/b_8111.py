from collections import deque

n = int(input())
tmp = 0

# K + (0 or 1) % N / K % N + (0 or 1) => result % N 결과는 양쪽 다 동일
# 나머지 저장 for 오버플로우 방지
def bfs():
    q = deque()

    # 1부터 시작
    q.append(1)
    ans_dict[1] = '1'
    v[1] = True
    parent[1] = -1

    while q:
        cur = q.popleft()
        tmp_list = [(cur * 10) % tmp, (cur * 10 + 1) % tmp] # 0 or 1 붙였을 때 나머지 수
        for i in range(2):
            # 기 등장한 '나머지' 수일 경우
            if v[tmp_list[i]]:
                continue

            # 첫 등장한 '나머지' 수일 경우
            parent[tmp_list[i]] = cur
            ans_dict[tmp_list[i]] = str(i) # 0 or 1 => 문자열로 저장 for 출력
            if tmp_list[i] == 0:
                return

            v[tmp_list[i]] = True
            q.append(tmp_list[i])

def print_ans(idx):
    if idx == -1:
        return

    print_ans(parent[idx])
    print(ans_dict[idx], end='')

for i in range(n):
    tmp = int(input())
    ans_dict = {}
    v = [False] * 20001
    parent = [0] * 20001
    bfs()
    print_ans(0)
    print()

# 6
# 17
# 11011
# 17
# 999
# 125
# 173