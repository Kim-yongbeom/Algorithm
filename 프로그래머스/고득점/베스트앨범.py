# 진행중
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
    # for i in answer.values():
    #     print(i)
    # dict값들 뽑아올수있음, 근데 만약
    # for i in range(answer.values()):
    #     print(answer.values()[i])
    # 해주는 거면 안됨
    #
    # dict 에서 .items()를 해주면 튜플 형태로 받아옴
    # 고유번호 4,1 번 더하고 3,0,2 더하게 만들어보자
    keyList = list(answer.keys())
    valueList = list(answer.values())

    return answer


# 진행중
def solution(genres, plays):
    answer = {}
    score = {}
    for idx, genre in enumerate(genres):
        key = genre
        value = plays[idx]
        if key in answer:
            answer[key].append(value)
        else:
            answer[key] = [value]

    for idx, genre in enumerate(set(genres)):
        # set은 중복은 없애주지만 인덱스 번호가 뒤죽박죽..
        score[genre] = sum(list(answer.values())[idx])
    print(score)
    print(answer)
