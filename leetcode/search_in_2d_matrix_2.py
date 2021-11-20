matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 100

# pythonic way => one line
print(any(target in row for row in matrix)) # any returns True if iterable has target
