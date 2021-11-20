nums = [4,5,6,0,1,2,3]
target = 0

# find pivot
left = 0
right = len(nums) - 1
while left < right:
    # mid = left + (right - left) // 2
    mid = (right + left) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

print(left)