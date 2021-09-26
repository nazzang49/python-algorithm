def remove_bug(sentence:str):
    tmp = ''
    while True:
        # replace => 현 시점 기준, pattern 에 해당하는 문자만 변경
        # if 변경 후에도 pattern 이 존재한다면 loop 필요
        sentence = sentence.replace('BUG', '')
        if sentence == tmp:
            print(sentence)
            break
        tmp = sentence

while True:
    try:
        remove_bug(input())
    except:
        break