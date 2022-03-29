# 내 코드
# 시간초과
import itertools


def solution(number, k):
    answer = ''
    a = itertools.combinations(number, len(number)-k)
    answer = max(list(map(''.join, a)))
    return answer

# 다른 사람 코드


def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])
