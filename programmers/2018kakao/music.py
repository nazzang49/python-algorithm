def solution(m, musicinfos):
    answer = [(0, '(none)')]
    for i, musicinfo in enumerate(musicinfos):
        tmp = musicinfo.split(',')
        s = tmp[0]
        e = tmp[1]
        title = tmp[2]
        info = change_sharp(tmp[3])

        time = (int(e[:2]) - int(s[:2])) * 60 + (int(e[3:5]) - int(s[3:5]))
        r = time // len(info)
        c = time % len(info)

        tmp_s = info * r + info[:c]
        m = change_sharp(m)
        if m in tmp_s and answer[0][0] < time:
            answer = [(time, title)]
    return answer[0][1]

def change_sharp(s):
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    s = s.replace('A#', 'a')
    return s