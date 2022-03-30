# 진행중
def solution(people, limit):
    answer = 0
    weight = 0

    while people:
        # limit와 같거나 더 큰사람 1명만 들어갈수있으므로
        if limit <= people[0]:
            people.pop(0)
            answer += 1
        elif limit > people[0]:
    return answer
