strs = ["eat","tea","tan","ate","nat","bat"]

# sort
vals = [(''.join(sorted(s)), s) for s in strs]
keys = set([''.join(sorted(s)) for s in strs])

ans = []
for k in keys:
    tmp = []
    for s in vals:
        if k == s[0]:
            tmp.append(s[1])
    ans.append(tmp)
print(ans)

############################################################################

# defaultdict
from collections import defaultdict

dd = defaultdict(list)
for word in strs:
    dd[''.join(sorted(word))].append(word)
print(dd.values())