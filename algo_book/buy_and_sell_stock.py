prices = [7,1,5,3,6,4]
import sys

# prices = [7,6,4,3,1]

# 2-pointer approach
left = 0
right = len(prices) - 1
ans = 0
while left < right:
    if prices[left] >= prices[right]:
        left += 1
    else:
        ans = max(ans, (prices[right] - prices[left]))
        right -= 1
print(ans)

# pythonic way
ans = 0
min_price = sys.maxsize

for price in prices:
    min_price = min(min_price, price) # min price update
    ans = max(ans, (price - min_price)) # current price - min price

print(ans)