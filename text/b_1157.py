def get_most_used_char(word):
    d = dict()
    word = word.upper()
    for c in word:
        if d.get(c):
            continue
        d[c] = word.count(c)

    # -- sorted => dict to list
    d = sorted(d.items(), key=lambda x:x[1], reverse=True)
    if d[0][1] == d[1][1]:
        return '?'
    return d[0][0]

word = input()
if len(word) == 1:
    print(word.upper())
print(get_most_used_char(word))