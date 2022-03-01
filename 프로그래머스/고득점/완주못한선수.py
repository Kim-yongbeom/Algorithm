# 2022-03-01
def solution(participant, completion):
    for person in completion:
        participant.remove(person)
        # remove 그대로 쓰면 리스트 형태로 나옴
        # 효울성 테스트 시간초과!!
    return participant[0]
    # participant.pop()랑 똑같다

# 내 다른 코드


def solution(participant, completion):
    for person in completion:
        # pop 안에는 int값만 들어갈 수 있음
        # 효울성 테스트 시간초과!!
        # 내가 생각하는 안되는 이유
        # 반복문을 다 돌리고 return을 해서 효율성이 많이 떨어지는 느낌 (반복문 안에도 값이 나오면 바로 return 하게 만들어 줘야 할듯)
        participant.pop(participant.index(person))
    return participant[0]


# 참고해서 푼 내 다른 코드
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for idx, person in enumerate(completion):
        if participant[idx] != person:
            return participant[idx]
    return participant[-1]


# 다른 사람 코드.
def solution(participant, completion):
    participant.sort()
    completion.sort()
    # zip 반복문 participant -> p, completion -> c
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()
