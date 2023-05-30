# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import defaultdict

def solution(clothes):
    answer = 1

    d = defaultdict(int)
    for clothe, type in clothes:
        d[type] += 1

    for k, v in d.items():
        answer *= (v + 1)

    # (!) -1 = non-clothes
    return answer - 1