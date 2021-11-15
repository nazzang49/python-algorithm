numCourses = 2
prerequisites = [[1, 0], [0, 2], [2, 3], [2, 4], [3, 4], [5, 6]]
v = [False] * len(prerequisites)

# method_1 => for loop (wrong approach)
import copy
def dfs(course, course_list:list):
    if course in copy.deepcopy(course_list): # circular case => pruning
        return False

    course_list.append(course)
    for i in range(len(prerequisites)):
        if not v[i] and prerequisites[i][0] == course:
            v[i] = True
            if not dfs(prerequisites[i][1], course_list):
                return False
    return True

print(dfs(prerequisites[0][0], []))

# method_2 => defaultdict (right approach)

from collections import defaultdict

dd = defaultdict(list)
for prev, later in prerequisites:
    dd[prev].append(later)

v = set()
c = set()

def new_dfs(i):
    if i in c: # circular => False
        return False

    if i in v: # already visit => True (e.g) [(2, 3), 4]
        return True

    c.add(i)
    for k in dd[i]: # next course
        if not new_dfs(k):
            return False

    c.remove(i) # no circular
    v.add(i)
    return True

for x in list(dd): # list(dict) => keys()
    if not new_dfs(x):
        print(False)
        exit()
print(True)
