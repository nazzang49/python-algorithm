n = int(input())
k_dict = dict()
ans_dict = dict()

for i in range(n):
    k_dict[i + 1] = list(map(int, input().split()))

def dfs(k, v, i, cnt, total):
    if cnt == 3:
        is_biggest_value(k, total)
        return
    for m in range(i, len(v)):
        dfs(k, v, m + 1, cnt + 1, total + v[m])

def is_biggest_value(k, total):
    total = str(total)
    n_of_last = total[len(total) - 1]
    n_of_last = int(n_of_last)
    if ans_dict.get(k) is None:
        ans_dict[k] = n_of_last
        return
    if ans_dict[k] < n_of_last:
        ans_dict[k] = n_of_last

def get_final_ans():
    ans_list = sorted(ans_dict.items(), key=lambda x: x[1], reverse=True)
    ans_idx = ans_list[0][0]
    ans_val = ans_list[0][1]

    for v in ans_list:
        if v[1] == ans_val and v[0] > ans_idx:
            ans_idx = v[0]
    return ans_idx

for k, v in k_dict.items():
    dfs(k, v, 0, 0, 0)

print(get_final_ans())