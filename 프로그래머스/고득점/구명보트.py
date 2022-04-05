# 내코드
# pop from an empty deque 오류
# 코드도 틀린것같음
from collections import deque
def solution(people, limit):
    answer = 0
    total = 0
    # [70, 50, 80, 50, 90, 40], 240, 3 새로운 테스트케이스 추가
    backup = deque()
    queue = deque(people)
    
    while queue:
        weight = queue.popleft()
        while total <= limit:
            total += weight
            if total > limit:
                total = 0
                if backup:
                    queue.appendleft(backup.popleft())
                answer += 1
                break
            weight = queue.popleft()
            backup.appendleft(weight)
    print(backup)
    return answer

# 다른사람코드
def solution(people, limit):
    people.sort()
    answer = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        answer += 1
        # j넣어준 이유는 오른쪽 리스트부터 더해주려고
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    return answer
