n = int(input())
pattern = input()
p_list = pattern.split('*')
len_f = len(p_list[0])
len_b = len(p_list[1])

def is_da_or_ne(s):
    if s[:len_f] == p_list[0] and s[-len_b:] == p_list[1] and len(''.join(p_list)) <= len(s):
        return 'DA'
    else:
        return 'NE'

for i in range(n):
    s = input()
    print(is_da_or_ne(s))