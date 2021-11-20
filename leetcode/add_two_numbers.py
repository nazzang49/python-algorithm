l1 = [2,4,3]
l2 = [5,6,4]

l1 = l1[::-1]
l2 = l2[::-1]

l1_num = int(''.join(map(str, l1)))
l2_num = int(''.join(map(str, l2)))

ans = l1_num + l2_num
tmp = [int(s) for s in str(ans)]
print(tmp[::-1])