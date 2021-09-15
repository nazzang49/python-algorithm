n_list = [int(s) for s in input()]

ans = n_list[0]
for i in range(1, len(n_list)):
    # 현 시점 기준 최대값을 가지는 경우 선택
    ans = max(ans + n_list[i], ans * n_list[i])
print(ans)