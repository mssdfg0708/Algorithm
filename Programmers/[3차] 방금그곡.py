def calculate_time(start, end):
    start_time = int(start[0:2]) * 60 + int(start[3:])
    end_time = int(end[0:2]) * 60 + int(end[3:])

    return end_time - start_time


def solution1(m, musicinfos):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    candidate = -1
    for index in range(len(musicinfos)):
        start, end, name, music_info = musicinfos[index].split(',')
        music_info = music_info.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        play_time = calculate_time(start, end)

        # 실제 재생된 음악 정보 만들기
        i = 0
        play_info = ''
        while i < play_time:
            play_info += music_info[i % len(music_info)]
            i += 1

        if m in play_info:
            start, end, name, music_01 = musicinfos[candidate].split(',')
            start, end, name, music_02 = musicinfos[index].split(',')
            music_01 = music_01.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
            music_02 = music_02.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
            if candidate < 0:
                candidate = index
            elif len(music_01) > len(music_02):
                candidate = index

    if candidate >= 0:
        start, end, name, music_info = musicinfos[candidate].split(',')
        return name
    else:
        return "(None)"


def replacesharp(s):
    return s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def caltime(t):
    a = list(map(int, t.split(":")))
    return a[0]*60+a[1]


def splitinfo(infos):
    playtime = caltime(infos[1])-caltime(infos[0])
    sheet = replacesharp(infos[3])
    a, b = divmod(playtime, len(sheet))
    sheet = sheet*a+sheet[:b]
    return [playtime, infos[2], "".join(sheet)]


def solution2(m, musicinfos):
    infos = [splitinfo(info.split(",")) for info in musicinfos]
    print(infos)
    infos = [[idx]+i for idx, i in enumerate(infos) if replacesharp(m) in i[2]]
    try:
        return sorted(infos, key=lambda x: (x[1], -x[0]))[-1][2]
    except:
        return '(None)'


m = "C#D#"
musicinfos = ["12:00,12:14,HELLO,C#D#F#", "13:00,13:05,WORLD,ABCDEF"]
print(solution2(m, musicinfos))
