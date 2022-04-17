# 내 코드
# 1개 맞음..
from collections import deque


def solution(prices):
    answer = []
    d = deque([i for i in prices])
    while d:
        price = d.popleft()
        score = 0
        for idx in range(len(prices)-len(d), len(prices)):
            if prices[idx] >= price:
                score += 1
        answer.append(score)
    return answer


# queue (FIFO)


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer
