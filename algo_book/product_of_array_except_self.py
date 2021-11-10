nums = [1,2,3,4]

out = []
p = 1
for i in range(len(nums)):
    out.append(p)
    p *= nums[i]

p = 1
for i in range(len(nums) - 1, -1, -1):
    out[i] *= p # self = 1
    p *= nums[i]

print(out)