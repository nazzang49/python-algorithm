def get_max_score():
    tmp_list = [0 for _ in range(1000)]

    for i in range(n):
        # 현재 마감일 기준 => 더 짧은 마감일에 내림차순 정렬된 점수를 차례로 저장
        for j in range(scores[i][0] - 1, -1, -1):
            if tmp_list[j] == 0:
                tmp_list[j] = scores[i][1]
                break
    return sum(tmp_list)

n = int(input())
scores = []

for _ in range(n):
    d, s = map(int, input().split())
    scores.append((d, s))

scores = sorted(scores, key=lambda x: x[1], reverse=True)
print(get_max_score())