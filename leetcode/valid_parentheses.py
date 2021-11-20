s = "{[]}{}{}{}[][][][][[[[]]]]()()((({})))}}"

# use dict
d = {
    '{': '}',
    '[': ']',
    '(': ')'
}

stack = []
for b in s:
    if b in d:
        stack.append(b)
    elif not stack and d[stack.pop()] != b: # if stack exist
        print(False)
        exit()
if stack:
    print(False)
else:
    print(True)