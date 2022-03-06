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
    returns = []
    for idx, genre in enumerate(genres):
        key = genre
        value = plays[idx]
        if key in answer:
            answer[key].append(value)
        else:
            answer[key] = [value]
    setGenres = sorted(set(genres))
    # sort 해주는 이유는 set하면 중복 제거는 되지만 계속 값들이 실행할때마다 뒤죽박죽
    # sort해준 값을 .index로 해주어서 원하는 장르의 값을 더해주도록 해줌
    for idx, genre in enumerate(setGenres):
        score[genre] = sum(list(answer.values())[list(setGenres).index(genre)])
        if score[list(score)[idx]] > score[list(score)[idx-1]]:
            returns.append(plays.index(sorted(map(int, answer[genre]))[idx]))
            returns.append(plays.index(sorted(map(int, answer[genre]))[idx-1]))
        else:
            returns.append(plays.index(sorted(map(int, answer[genre]))[idx]))
            returns.append(plays.index(sorted(map(int, answer[genre]))[idx-1]))
    # 실행한 결괏값 [2,3,4,1]이(가) 기댓값 [4,1,3,0]와(과) 다릅니다.
    return returns


# 다른 사람 풀이
def solution(genres, plays):
    # genre_score : 각 장르별 속한 노래의 총 점수를 저장하는 딕셔너리
    # chk : 노래의 고유번호를 key 값으로 사용하고, value로 [해당 노래가 속한 장르의 점수, 해당 노래의 개별 점수]를 저장
    genre_score = dict()
    chk = dict()

    for i in range(len(genres)):
        # get() : 첫 번째 인자로는 찾고자 하는 키를 넣는다, 콤마(,)를 하고 두 번째 인자로는 첫 번째 인자에서 넣은 키가 없을 때 넣고자 하는 값을 넣는다.
        # 첫 번째 인자의 키의 값이 있을 경우는 그대로 그 값을 불러온다
        genre_score[genres[i]] = genre_score.get(genres[i], 0) + plays[i]
        # 500, 600, 650, 1450, 3100 가 순차적으로 저장됨
        # 최종 값은 1450, 3100 두 가지 장르의 총 점수들이 각각 저장됨

    for i in range(len(genres)):
        chk[i] = [genre_score[genres[i]], plays[i]]
        # [1450, 500], [3100, 600], [1450, 150], [1450, 800], [3100, 2500]
        # print(chk) = {0: [1450, 500], 1: [3100, 600], 2: [1450, 150], 3: [1450, 800], 4: [3100, 2500]}

    # sorted 안에서 람다식을 key=lambda x: (x[1], -x[0]), reverse=True
    # 이렇게 설정하면 chk의 점수로 내림차순 정렬된 후 고유 번호로 오름차순 정렬됩니다.
    # 이렇게 하면 2번 기준인 장르 내 많이 재생된 노래 순으로 1차적으로 정렬되고,
    # 고유 번호 기준 오름차순 조건에 따라 같은 재생 횟수가 있는 경우 고유 번호가 낮은 노래가 앞으로 오게 됩니다.

    # print(chk.items()) = 	dict_items([(0, [1450, 500]), (1, [3100, 600]), (2, [1450, 150]), (3, [1450, 800]), (4, [3100, 2500])])
    # lambda에 -를 붙이면 내림차순, +를 붙이면 오름차순으로 정렬됩니다. 물론 이 때 키는 숫자형 데이터타입이어야 합니다.
    chk = sorted(chk.items(), key=lambda x: (x[1], -x[0]), reverse=True)
    # print(chk) = [(4, [3100, 2500]), (1, [3100, 600]), (3, [1450, 800]), (0, [1450, 500]), (2, [1450, 150])]
    genre_score = sorted(genre_score.items(), key=lambda x: x[1], reverse=True)
    # print(genre_score) = [('pop', 3100), ('classic', 1450)]
    start = 0
    res = list()
    for gs in genre_score:
        cnt = 0
        for i in range(start, len(chk)):
            if chk[i][1][0] == gs[1] and cnt < 2:
                res.append(chk[i][0])
                cnt += 1

    return res
