tmp_list = input().split()
L = tmp_list[0]
R = tmp_list[1]

# 자릿수 다름 => 무조건 8이 없는 숫자 존재
# 첫자리 다름 => 무조건 8이 없는 숫자 존재
if len(L) != len(R) or L[0] != R[0]:
    print(0)
    exit()

# L이 기준
ans = 0
if L[0] == '8':
    ans += 1

for i in range(1, len(L)):
    # 같은 자리 수가 다름 => 더이상 8이 없는 숫자 존재
    if L[i] != R[i]:
        break
    # 같은 자리 수가 같음 => 8이 아니면 다음 자리 수 확인
    else:
        if L[i] == '8':
            ans += 1
print(ans)
