# 내코드 87.5점
def solution(fees, records):
    answer = []
    num = ''
    in_time, sum_time = 0, 0
    lists = []
    records.sort(key = lambda x: x.split()[1])
    
    for i in records:
        a = i.split()
        if num != a[1]:
            if in_time:
                sum_time += ((23 * 60 + 59)-(h + m))
                in_time = 0
            lists.append(sum_time)
            sum_time = 0
            num = a[1]
            
        time = list(map(int,a[0].split(':')))
        h = time[0] * 60
        m = time[1]
                
        if a[2] == 'IN':
            state = 'IN'
            in_time += h + m
            
        elif a[2] == 'OUT':
            state = 'OUT'
            sum_time += ((h + m) - in_time)
            in_time = 0
    # 마지막 num의 sum_time은 append 되지 않았으므로 반복문 밖에서 넣어줘야함        
    if state == 'OUT':
        lists.append(sum_time)
    elif state == 'IN':
        sum_time += ((23 * 60 + 59)-(h + m))
        lists.append(sum_time)
    lists.pop(0)
    
    for i in lists:
        result = 0
        if i-fees[0] > 0:
            if (i - fees[0]) % fees[2] == 0:
                result = (i - fees[0]) // fees[2]
            else:
                result = (i - fees[0]) // fees[2] + 1
        answer.append(fees[1]+(result*fees[3]))
    
    return answer


# 다른사람코드
import math

# 시간을 분으로 만들기
def dateToMinutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees
    
    dic = dict()

    for r in records:
        time, number, history = r.split()
        number = int(number)
        
        if number in dic:
            dic[number].append([dateToMinutes(time), history])
        else:
            dic[number] = [[dateToMinutes(time), history]]
    
    # 뽑아내기 쉽게 리스트로 만든것 같다.
    rList = list(dic.items())
    rList.sort(key=lambda x : x[0])
    
    for r in rList:
        t = 0
        print(r)
        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]

        if r[1][-1][1] == "IN":
            t += dateToMinutes('23:59')
        
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t-dt) / ut) * uf)        

    return answer