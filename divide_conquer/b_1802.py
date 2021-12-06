# 3
# 0
# 000
# 1000110

n = int(input())
def check(s, m_idx):
    for i in range(m_idx):
        if s[i] == s[m_idx * 2 - i]:
            return False
    return True

def is_possible(s):
    if len(s) == 1:
        return True

    m_idx = len(s) // 2

    if not check(s, m_idx):
        return False
    if not is_possible(s[:m_idx]):
        return False
    if not is_possible(s[m_idx + 1:]):
        return False
    return True

for _ in range(n):
    if is_possible(input()):
        print('YES')
    else:
        print('NO')