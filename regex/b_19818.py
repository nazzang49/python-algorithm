import re

ref_list = []
desc_dict = {}
while True:
    sentence = input()
    if sentence.startswith('\\end'):
        break

    for word in sentence.split():
        if '\\cite' in word or '\\bibitem' in word:
            p = re.compile('\{.*\}')
            m = p.search(word)
            if m:
                tmp = m.group()
                if '\\cite' in word:
                    ref_list.append(tmp[1:-1])
                else:
                    desc_dict[tmp[1:-1]] = sentence

flag = True
for i, (k, v) in enumerate(desc_dict.items()):
    if ref_list[i] != k:
        flag = False
        break

if flag:
    print('Correct')
else:
    print('Incorrect')
    print('\\begin{thebibliography}{99}')
    for ref in ref_list:
        print(desc_dict[ref])
    print('\\end{thebibliography}')