nums = [6,2,6,5,1,2]
nums.sort()

arr = []
for i in range(len(nums)):
    if i % 2 == 0:
        arr.append(nums[i])

print(sum(arr))

# pythonic way => sorted result = list
ans = sum(sorted(nums)[::2])
print(ans)