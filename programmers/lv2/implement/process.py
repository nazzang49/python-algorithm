# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0

    pairs = [[priorities[i], i] for i in range(len(priorities))]
    q = deque(pairs)
    while q:
        flag = False
        priority, loc = q.popleft()
        for nx_priority, nx_loc in q:
            if priority < nx_priority:
                flag = True
                q.append([priority, loc])
                break

        if not flag:
            answer += 1
            if loc == location:
                return answer

    return answer
