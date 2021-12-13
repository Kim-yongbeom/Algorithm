# https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    participant.sort()
    completion.sort()
    # zip 반복문 participant -> p, completion -> c
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()
