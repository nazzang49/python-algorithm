import numpy as np

zero = 0
one = 0

def solution(arr):
    arr = np.array(arr)
    is_compressible(arr)
    return [zero, one]

def is_compressible(arr):
    global zero, one
    l = len(arr)
    n = arr[0][0]

    flag = False
    for i in range(l):
        for j in range(l):
            if n != arr[i][j]:
                flag = True
                break
        if flag:
            break
    if flag:
        # when numpy, 2d-array slicing is possible
        is_compressible(arr[:l // 2, :l // 2])
        is_compressible(arr[:l // 2, l // 2:l])
        is_compressible(arr[l // 2:l, :l // 2])
        is_compressible(arr[l // 2:l, l // 2:l])
    else:
        if n:
            one += 1
        else:
            zero += 1

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))