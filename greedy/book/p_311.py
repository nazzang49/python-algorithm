n = int(input())
fear = [int(s) for s in input().split()]
fear.sort()
print(fear)

ans = 0
cnt = 0
for i in fear:
    # 인원수 한명씩 증가하면서 (현재 기준) 그룹 형성 가능한지 확인 => 최소 조건 만족 시 바로 그룹 형성 => 최대 그룹 도출 가능
    cnt += 1
    if cnt >= i:
        ans += 1
        cnt = 0
print(ans)