n = int(input())

import re

def is_pattern(s):
    p = re.compile('(100+1+|01)+')

    # match => 부분 match
    # fullmatch => 전체 match
    m = p.fullmatch(s)
    if m:
        return True
    return False

for i in range(n):
    if is_pattern(input()):
        print('YES')
    else:
        print('NO')