paths = []

def solution(dirs):
    x, y = 0, 0
    for dir in dirs:
        if dir == 'U':
            if not is_movable(x, y + 1):
                continue
            if not (x, y, x, y + 1) in paths:
                paths.append((x, y, x, y + 1))
                paths.append((x, y + 1, x, y))
            y += 1
        elif dir == 'R':
            if not is_movable(x + 1, y):
                continue
            if not (x, y, x + 1, y) in paths:
                paths.append((x, y, x + 1, y))
                paths.append((x + 1, y, x, y))
            x += 1
        elif dir == 'L':
            if not is_movable(x - 1, y):
                continue
            if not (x, y, x - 1, y) in paths:
                paths.append((x, y, x - 1, y))
                paths.append((x - 1, y, x, y))
            x -= 1
        else:
            if not is_movable(x, y - 1):
                continue
            if not (x, y, x, y - 1) in paths:
                paths.append((x, y, x, y - 1))
                paths.append((x, y - 1, x, y))
            y -= 1
    return len(paths) // 2

def is_movable(x, y):
    if x < -5 or x > 5 or y < -5 or y > 5:
        return False
    return True

print(solution("ULURRDLLU"))