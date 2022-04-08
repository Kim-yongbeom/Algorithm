# https://programmers.co.kr/learn/courses/30/lessons/12977
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(nums):
    answer = 0
    sum = 0
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if is_prime_number(sum):
                    answer += 1
    return answer

# 다른사람 코드
# combinations 라이브러리 사용
from itertools import combinations 
def check(a, b, c): 
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A: 
        if check(i[0], i[1], i[2]): answer += 1
    return answer
