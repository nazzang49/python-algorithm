s = 'abbdddccc'
alpha = [0] * 26

# ord => ascii code in python
for t in s:
    alpha[ord(t) - ord('a')] += 1

ans = ''
for i, c in enumerate(alpha):
    if c > 0:
       ans += chr(i + ord('a'))

print(ans)