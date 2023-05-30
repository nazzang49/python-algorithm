# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import Counter


def solution(want, number, discount):
    answer = 0

    d = {
        w: n for w, n in zip(want, number)
    }

    for i in range(len(discount) - 9):
        c = Counter(discount[i:i + 10])
        if c == d:
            answer += 1

    return answer