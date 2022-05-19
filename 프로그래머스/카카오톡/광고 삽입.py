#다른사람코드
def solution(play_time, adv_time, logs):    
    timeblock_logs = []
    pl = time_to_num(play_time)
    ad = time_to_num(adv_time)
    clock = [0 for _ in range(pl+1)]

    for i, log in enumerate(logs):
        start = time_to_num(log[:8])
        end = time_to_num(log[9:])
        clock[start] += 1
        clock[end] -= 1

    for i in range(1, len(clock)):          # 초당 시청자 수
        clock[i] += clock[i-1]

    for i in range(1, len(clock)):          # 초단위 누적 시청자 수
        clock[i] += clock[i-1]

    largest_view = clock[ad-1]              # 00:00:00 ~ ad 까지의 시청자 수
    time_large_view = 0
    for end_minus1 in range(ad, pl):
        if largest_view < clock[end_minus1]-clock[end_minus1-ad]:
            largest_view = clock[end_minus1]-clock[end_minus1-ad]
            time_large_view = end_minus1+1 - ad
    return num_to_time(time_large_view)

def time_to_num(hhmmss):
    hours, minutes, seconds = hhmmss.split(':')
    return 3600*int(hours) + 60*int(minutes)+int(seconds)

def num_to_time(num):
    hours = "0"+str(num//3600)
    minutes = "0"+str((num%3600) // 60)
    seconds = "0"+str((num%3600)%60)
    return ":".join([hours[-2:],minutes[-2:],seconds[-2:]])