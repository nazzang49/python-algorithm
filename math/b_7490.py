import copy

ans_dict = dict()
n = int(input())

def is_zero(op_term, num_list):
    tmp = ''
    len_num_list = len(num_list)
    for i in range(len_num_list - 1):
        tmp += str(num_list[i]) + op_term[i]
    tmp += str(num_list[-1])
    ans = ''.join(tmp.split())
    if eval(ans) == 0:
        print(tmp)

def dfs(op_list, m):
    if len(op_list) == m:
        cat_op_list.append(copy.deepcopy(op_list))
        return

    op_list.append(' ')
    dfs(op_list, m)
    op_list.pop()

    op_list.append('+')
    dfs(op_list, m)
    op_list.pop()

    op_list.append('-')
    dfs(op_list, m)
    op_list.pop()

for k in range(n):
    m = int(input())
    cat_op_list = []
    op_list = []
    dfs(op_list, m - 1)

    num_list = [i for i in range(1, m + 1)]
    for op_term in cat_op_list:
        is_zero(op_term, num_list)
    print()