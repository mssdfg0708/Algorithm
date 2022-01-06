def calculate_time(start, end):
    start_time = int(start[0:2]) * 60 + int(start[3:])
    end_time = int(end[0:2]) * 60 + int(end[3:])

    return end_time - start_time


def solution(m, musicinfos):
    candidate = -1
    for index in range(len(musicinfos)):
        start, end, name, music_info = musicinfos[index].split(',')
        play_time = calculate_time(start, end)

        # 실제 재생된 음악 정보 만들기
        i = 0
        play_info = ''
        while i < play_time:
            play_info += music_info[i % len(music_info)]
            if music_info[(i + 1) % len(music_info)] == '#':
                play_time += 1
            i += 1

        if m in play_info:
            start, end, name, len01 = musicinfos[candidate].split(',')
            start, end, name, len02 = musicinfos[index].split(',')
            if candidate < 0:
                candidate = index
            elif len01 > len02:
                candidate = index

    if candidate >= 0:
        start, end, name, music_info = musicinfos[candidate].split(',')
        return name
    else:
        return "None"


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
