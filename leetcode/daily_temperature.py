temperatures = [73,74,75,71,69,72,76,73]

# bruteforce
out = [0] * len(temperatures)
for i in range(len(temperatures) - 1):
    for j in range(i + 1, len(temperatures)):
        if temperatures[i] < temperatures[j]:
            out[i] += (j - i)
            break

print(out)

# stack
stack = []
out = [0] * len(temperatures)
for i, t in enumerate(temperatures):
    while stack and temperatures[stack[-1]] < t: # always last is criteria
        last = stack.pop() # current > last => pop and out[last] update
        out[last] = (i - last) # 75 met 76 => (6 - 2)
    stack.append(i)

print(out)