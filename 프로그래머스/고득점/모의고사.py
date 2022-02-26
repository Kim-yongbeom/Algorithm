# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    score = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        #############
        # 이 부분 안넣어주면 런타임에러 발생
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        #############
        if a[s1] == answers[i]:
            score[0] += 1
        if b[s2] == answers[i]:
            score[1] += 1
        if c[s3] == answers[i]:
            score[2] += 1
    max_score = max(score[0], score[1], score[2])
    if max_score == score[0]:
        answer.append(1)
    if max_score == score[1]:
        answer.append(2)
    if max_score == score[2]:
        answer.append(3)
    return answer


# 2022-02-26 진행중인 코드
def solution(answers):
    answer = []
    score1 = 0
    score2 = 0
    score3 = 0
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in enumerate(answers):
        if people1[i[0]] == i[1]:
            score1 += 1
        if people2[i[0]] == i[1]:
            score2 += 1
        if people3[i[0]] == i[1]:
            score3 += 1

    return answer


# 다른사람 코드
def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
# https://jongminfire.dev/%ED%8C%8C%EC%9D%B4%EC%8D%AC-enumerate-zip
# enumerate() 함수는 인자의 값을 추출 할 때 인덱스를 추출하는 기법이다. 함수를 사용하면 인덱스 번호와 컬렉션의 원소를 튜플 형태로 반환한다.
# idx는 인덱스 번호를 할당 받고, answer는 값을 받음
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
