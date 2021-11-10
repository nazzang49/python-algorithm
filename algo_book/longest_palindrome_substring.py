import re

s = "cbbd"
s.lower()
s = re.sub('[^a-z0-9]', '', s)

# 2-pointer => symmetric sequence
def get_palindrome(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

if len(s) < 2 or s == s[::-1]:
    print(s)
else:
    ans = ''
    for i in range(1, len(s) - 1):
        ans = max(ans, get_palindrome(s, i, i + 1), get_palindrome(s, i, i + 2), key=len)
print(ans)

# i + 1 => all chars are same
# i + 2 => all chars are same except the center