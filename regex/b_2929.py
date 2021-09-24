s = input()

def calc_mod(cnt):
    cnt %= 4
    if cnt != 0:
        cnt = 4 - cnt
    return cnt

s_len = len(s)
ans = 0
for i in range(s_len):
    if s[i].isupper():
        cnt = 0
        for j in range(i + 1, s_len):
            cnt += 1
            if s[j].isupper():
                ans += calc_mod(cnt)
                break

print(ans)