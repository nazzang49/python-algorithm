from collections import defaultdict

n, m, k = map(int, input().split())
scores = defaultdict()
for i in range(n):
    scores[i + 1] = 0

for i in range(m):
    tmp_list = list(map(float, input().split()))
    for j in range(0, len(tmp_list) - 1, 2):
        # 현재 장르에 대한 점수 > 기존 점수
        if tmp_list[j + 1] > scores[tmp_list[j]]:
            scores[tmp_list[j]] = tmp_list[j + 1]

ans = sorted(list(scores.values()), reverse=True)
ans = sum(ans[:k])
print(f'{ans:.1f}')