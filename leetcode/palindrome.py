import re

# slicing is better than list and deque
s = 'teet'
s.lower()
s = re.sub('[^a-z0-9]', '', s)
print(s == s[::-1])