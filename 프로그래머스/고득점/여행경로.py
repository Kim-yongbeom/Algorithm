# 진행중
from collections import deque


def solution(tickets):
    answer = []
    same = []
    q = deque()
    for i in range(len(tickets)):
        q.append([tickets[i][0], tickets[i][1]])
    V = [0 for i in range(len(tickets))]

    while True:
        start, target = q.popleft()
        for i in range(len(tickets)):
            if start == tickets[i][0]:
                same.append(tickets[i][1])
                same = sorted(same)
        # target를 어떻게 바꿔줄지 생각해보기
        # tickets[i]를 통해 target값을 반복 조회
        # start가 ICN 말고 다른 출발지도 같을 경우도 생각해야함
        if target == same[0]:
            print(target)

        break

    return answer
