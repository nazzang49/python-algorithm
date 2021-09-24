import re
n = int(input())

# [abc] => a, b, c 중 어떤 문자든 가능
# + => 최소 1회 이상 반복
# * => 최소 0회 이상 반복
# ? => 0 or 1회
# {n, m} => n ~ m 회 반복

# match => index 0부터 탐색
# search => index 관계없이 탐색
# m.group() => 실제 매칭되는 패턴 추출

def is_valid_pattern(pattern):
    # 문제의 조건 => 정규식으로 변환
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