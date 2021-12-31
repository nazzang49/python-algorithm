# chr(65) = 'A'
def solution(msg):
    answer = []
    indices = {chr(65 + i): i + 1 for i in range(26)}
    while msg:
        idx = 1
        while indices.get(msg[:idx]) and idx <= len(msg):
            idx += 1
        idx -= 1
        answer.append(indices[msg[:idx]])
        indices[msg[:idx + 1]] = len(indices) + 1
        msg = msg[idx:]
    return answer

print(solution('KAKAO'))
