# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    answer = 0
    for i in range(10):
        if i in numbers:
            answer += 0
        else:
            answer += i
    return answer

# 다른 사람 코드
def solution(numbers):
    return 45 - sum(numbers)