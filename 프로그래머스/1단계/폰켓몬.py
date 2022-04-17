from itertools import combinations


def solution(nums):
    answer = 0
    tmp = 0
    num = set(nums)
    if len(num) >= len(nums)//2:
        for i in combinations(num, len(nums)//2):
            score = len(set(i))
            if score == len(nums)//2:
                answer = score
                break
            elif score > tmp:
                answer = score
                tmp = score
    else:
        for i in combinations(num, len(num)):
            score = len(set(i))
            if score == len(nums)//2:
                answer = score
                break
            elif score > tmp:
                answer = score
                tmp = score
    return answer
