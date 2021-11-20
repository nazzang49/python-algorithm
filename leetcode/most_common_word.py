import re
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

paragraph = paragraph.lower()
paragraph = re.sub('[^\w]', ' ', paragraph) # \w => only word characters

for b in banned:
    paragraph = re.sub(b, '', paragraph)
print(Counter(paragraph.split()).most_common()[0][0])


########################################################################

# list comprehension => pythonic way
words = [word for word in paragraph.split() if word not in banned]
print(Counter(words).most_common()[0][0])
