import re
n = int(input())

def is_valid_pattern(pattern):
    cp = re.compile('[A-F]?A+F+C+[A-F]?')
    m = cp.match(pattern)
    if m and len(m.group()) == len(pattern):
        return True
    return False

for i in range(n):
    if is_valid_pattern(input()):
        print('Infected!')
    else:
        print('Good')