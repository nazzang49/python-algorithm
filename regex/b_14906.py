import re

n = int(input())

# 스림프
def is_slimp(s):
    s_len = len(s)
    if s_len == 2:
        if s == 'AH':
            return True
    elif s_len > 2:
        if s[:2] == 'AB' and s[-1] == 'C':
            if is_slimp(s[2:-1]):
                return True
        if s[:2] == 'AD' or s[:2] == 'AE' and s[-1] == 'C':
            if is_slump(s[1:-1]):
                return True
    return False

# 스럼프
def is_slump(s):
    p = re.compile("([DE]F+)+G$")
    if p.match(s):
        return True
    return False

print('SLURPYS OUTPUT')
for i in range(n):
    s = input()
    flag = False
    for j in range(1, len(s)):
        # 최종 형태 => 스림프 + 스러피
        if is_slimp(s[:j]) and is_slump(s[j:]):
            flag = True
    if flag:
        print('YES')
    else:
        print('NO')

print('END OF OUTPUT')