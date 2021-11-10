s = "cbacdcbc"

# solved by stack
from collections import Counter

counter = Counter(s)
stack = []

for c in s: # c => current character in s
    counter[c] -= 1
    if c in stack:
        continue
    while stack and c < stack[-1] and counter[stack[-1]] > 0: # previous char => check order + check duplicate
        stack.pop()
    stack.append(c)
print(''.join(stack))