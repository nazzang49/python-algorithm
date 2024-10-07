# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100

arr = [int(input()) for _ in range(10)]
ans = 0

# (방법 1)
for e in arr:
    if abs(100 - ans) >= abs(100 - (ans + e)):
        ans += e
    else:
        break

# (방법 2)
# for i in range(10):
#     total = sum(arr[:i])
#     if abs(100 - ans) >= abs(100 - total):
#         ans = total
#     else:
#         break

print(ans)



