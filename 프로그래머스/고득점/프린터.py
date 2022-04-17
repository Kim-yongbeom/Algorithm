# 내 코드
# answer 를 어떻게 설정해줘야할지 모르겠다.
# dict로 ?
def solution(priorities, location):
    answer = 0
    score = 0
    for i in range(len(priorities)):
        if priorities.index(max(priorities)) == 0:
            print(priorities)
            break
        priorities.append(priorities.pop(0))
        score += 1
    answer = len(priorities) - score + 1
    return answer

# 다른 사람 코드


def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        # d and 부분이 없으면 런타임에러 발생
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
