# 효율성 테스트 한문제 시간초과
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3
    return answer

# 다른 코드
def solution(n):
    answer = ''
    while n>0:
        if n%3 == 0:
            answer = '4'+answer
            n = n//3 -1
        else:
            answer = str(n%3) + answer
            n = n//3
        
    return answer
