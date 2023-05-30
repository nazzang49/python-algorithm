# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []

    s = s.strip("{{}}")
    arr = [list(map(int, c.split(","))) for c in s.split("},{")]
    arr.sort(key=lambda x: len(x))

    for a in arr:
        for n in a:
            if n not in answer:
                answer.append(n)

    return answer