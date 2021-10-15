n = int(input())
dp = [[-1] * 1000] * 1000

# 소수 판별
def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return 0
        i += 1
    return 1

# 1, 2번 저금통 숫자 concat
def concat_integer(x, y):
    x = str(x)
    y = str(y)
    return int(x + y)

# 1, 2번 저금통 숫자 dp by 재귀
def check_dp(x, y):
    # out range
    if x > n or y > n:
        return 0

    # last
    if x == n and y == n:
        return is_prime(concat_integer(x, y))

    cnt = is_prime(concat_integer(x, y))
    cnt += max(check_dp(x + 1, y), check_dp(x, y + 1)) # 1, 2번 저금통 중 어느 쪽을 넣어주는 것이 가장 이득인지
    return cnt

print(check_dp(1, 1) - 1) # (1, 1) 제외