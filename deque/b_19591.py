from collections import deque
import sys

digits = deque()
ops = deque()

s = sys.stdin.readline()
tmp = ''
if s[0] == '-':
    tmp += '-'
    s = s[1:]

for c in s:
    if c.isdigit():
        tmp += c
    else:
        digits.append(int(tmp))
        tmp = ''
        ops.append(c)

ops.pop()

if not ops:
    print(digits.popleft())
else:
    while len(digits) > 1:
        left1 = digits[0]
        left2 = digits[1]

        right2 = digits[-1]
        right1 = digits[-2]

        left_op = ops[0]
        right_op = ops[-1]

        if left_op in ['*', '/'] and right_op in ['+', '-']:
            digits.popleft()
            digits.popleft()
            ops.popleft()
            if left_op == '*':
                digits.appendleft(left1 * left2)
            else:
                digits.appendleft(int(left1 / left2))
        elif right_op in ['*', '/'] and left_op in ['+', '-']:
            digits.pop()
            digits.pop()
            ops.pop()
            if right_op == '*':
                digits.append(right1 * right2)
            else:
                digits.append(int(right1 / right2))
        else:
            if left_op in ['+', '-']:
                tmp_left = left1 + left2 if left_op == '+' else left1 - left2
                tmp_right = right1 + right2 if right_op == '+' else right1 - right2
            else:
                tmp_left = left1 * left2 if left_op == '*' else int(left1 / left2)
                tmp_right = right1 * right2 if right_op == '*' else int(right1 / right2)

            if tmp_left >= tmp_right:
                digits.popleft()
                digits.popleft()
                ops.popleft()
                digits.appendleft(tmp_left)
            else:
                digits.pop()
                digits.pop()
                ops.pop()
                digits.append(tmp_right)

    print(digits.popleft())
