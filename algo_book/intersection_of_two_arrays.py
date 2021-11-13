nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1 = list(set(nums1))
nums2 = list(set(nums2))

nums1.sort()
nums2.sort()

ans = []
for n1 in nums1:
    left = 0
    right = len(nums2) - 1
    while left <= right and right >= 0:
        mid = left + (right - left) // 2
        if nums2[mid] < n1:
            left = mid + 1
        elif nums2[mid] > n1:
            right = mid - 1
        else:
            ans.append(n1)
            break
print(ans)