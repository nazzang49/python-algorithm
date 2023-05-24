# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0

    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations[i:]):
            return len(citations[i:])

    return answer