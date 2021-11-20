
# 2-pointer approach
height = [0,1,0,2,1,0,1,3,2,1,2,1]

total = 0
left = 0
right = len(height) - 1
max_left = height[left]
max_right = height[right]
while left < right:
    max_left = max(max_left, height[left])
    max_right = max(max_right, height[right])

    # toward the center from left
    if max_left <= max_right:
        total += (max_left - height[left])
        left += 1
    # toward the center from right
    else:
        total += (max_right - height[right])
        right -= 1

print(total)