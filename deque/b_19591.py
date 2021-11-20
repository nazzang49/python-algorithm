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
    while ops:
        left1 = digits[0]
        left2 = digits[1]

        right2 = digits[-1]
        right1 = digits[-2]

        left_op = ops[0]
        right_op = ops[-1]

        tmp_left_digit = eval(str(left1) + left_op + str(left2))
        tmp_right_digit = eval(str(right1) + right_op + str(right2))

        if left_op == '/':
            tmp_left_digit = abs(left1) // abs(left2)
            if left1 < 0 or left2 < 0:
                tmp_left_digit = -tmp_left_digit

        if right_op == '/':
            tmp_right_digit = abs(right1) // abs(right2)
            if right1 < 0 or right2 < 0:
                tmp_right_digit = -tmp_right_digit

        if (left_op == '*' or left_op == '/') and (right_op == '+' or right_op == '-'):
            digits.popleft()
            digits.popleft()
            ops.popleft()
            digits.insert(0, tmp_left_digit)
        elif (right_op == '*' or right_op == '/') and (left_op == '+' or left_op == '-'):
            digits.pop()
            digits.pop()
            ops.pop()
            digits.append(tmp_right_digit)
        elif ((left_op == '*' or left_op == '/') and (right_op == '*' or right_op == '/'))\
                or ((left_op == '+' or left_op == '-') and (right_op == '+' or right_op == '-')):
            if tmp_left_digit > tmp_right_digit:
                digits.popleft()
                digits.popleft()
                ops.popleft()
                digits.insert(0, tmp_left_digit)
            elif tmp_right_digit > tmp_left_digit:
                digits.pop()
                digits.pop()
                ops.pop()
                digits.append(tmp_right_digit)
            else:
                digits.popleft()
                digits.popleft()
                ops.popleft()
                digits.insert(0, tmp_left_digit)

    print(digits.popleft())
