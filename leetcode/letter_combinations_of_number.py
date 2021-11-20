# digits = "23"
digits = "2"

ans = []
keypad = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}
def dfs(idx, s):
    if idx == len(digits):
        ans.append(s)
        return

    for c in keypad[digits[idx]]:
        dfs(idx + 1, s + c)

if digits == '1' or digits == '':
    print(ans)
else:
    dfs(0, '')

print(ans)