d = [1, 2, 3]
k = 2

# get test_indices
test_indices = []
d_len = len(d)
if d_len % k == 0:
    test_indices = [d_len // k for _ in range(k)]
else:
    for i in range(k):
        if i == k - 1:  # last
            test_indices.append(d_len)
        else:
            tmp = d_len // k
            test_indices.append(tmp)
            d_len -= tmp

print(test_indices)

# get train and test pair
ans = []
for n in test_indices:
    test_set = []
    for _ in range(n):
        tmp = d.pop()
        test_set.append(tmp)
    train_set = [idx for idx in d]
    ans.append(sorted(train_set))
    ans.append(sorted(test_set))
    d.insert(0, tmp) # rollback for another pair

print(ans)