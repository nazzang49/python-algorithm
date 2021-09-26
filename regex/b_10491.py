def is_problem(s):
    s = s.lower()
    if 'problem' in s:
        return 'yes'
    return 'no'

i = 0
while i <= 1000:
    try:
        print(is_problem(input()))
        i += 1
    except:
        break