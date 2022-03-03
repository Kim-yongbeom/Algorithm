def solution(genres, plays):
    answer = {}
    dic = {}
    for idx, genre in enumerate(genres):
        key = genre
        value = plays[idx]
        if key in answer:
            answer[key].append(value)
        else:
            answer[key] = [value]
    # 고유번호 4,1 번 더하고 3,0,2 더하게 만들어보자
    keyList = list(answer.keys())
    valueList = list(answer.values())

    return answer
