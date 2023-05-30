# https://school.programmers.co.kr/learn/courses/30/lessons/17677

from collections import defaultdict

def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    d_str1 = defaultdict(int)
    d_str2 = defaultdict(int)

    for i in range(len(str1) - 1):
        cur = str1[i:i + 2]
        if cur.isalpha() and ' ' not in cur:
            d_str1[cur] += 1

    for i in range(len(str2) - 1):
        cur = str2[i:i + 2]
        if cur.isalpha() and ' ' not in cur:
            d_str2[cur] += 1

    if len(d_str1) == 0 and len(d_str2) == 0:
        return 65536

    unique = 0
    total = 0

    for k in d_str1.keys():
        unique += min(d_str1[k], d_str2[k]) if d_str2[k] != 0 else 0
        total += max(d_str1[k], d_str2[k])

    for k in d_str2.keys():
        total += d_str2[k] if d_str1[k] == 0 else 0

    answer = int((unique / total) * 65536)
    return answer