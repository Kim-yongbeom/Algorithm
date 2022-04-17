# 내 코드

def solution(numbers):
    answer = 0
    numberList = []

    for i in range(len(numbers)-1):
        numberList.append(numbers[i])
        numberList.append(numbers[i+1])
        numberList.append(numbers[i] + numbers[i+1])
        numbers = sorted(numbers, reverse=True)
        numberList.append(numbers[i])
        numberList.append(numbers[i+1])
        numberList.append(numbers[i] + numbers[i+1])

    for i in range(2, len(set(numberList))):
        print(list(set(numberList)))
        # ['1', '7', '17', '71']
        # ['1', '10', '01', '11', '0']
        # 101이 없음
    return answer


# 다른 사람 코드
# import math
# from itertools import permutations
def is_prime_number(n):
    """소수판별 함수"""
    if n == 0 or n == 1:                                # 0,1 은 소수가 아님
        return False
    else:
        # sqrt(n)까지만 for문을 돌면서 확인하면 된다.
        # math.sqrt = 제곱근 구하기
        for i in range(2, int(math.sqrt(n)) + 1):
            # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
            if n % i == 0:
                return False

        return True                                 # for문을 다 돌았는데도 False가 아니면 소수


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        # permutations(순열)을 사용해 i개씩 묶어지는 list 생성
        arr = list(permutations(numbers, i))
        # arr = 	[('0',), ('1',), ('1',)]
        #           [('0', '1'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '0'), ('1', '1')]
        #           [('0', '1', '1'), ('0', '1', '1'), ('1', '0', '1'), ('1', '1', '0'), ('1', '0', '1'), ('1', '1', '0')]
        for j in range(len(arr)):                   # 생성한 list(arr) 길이만큼 for문 실행
            # len(arr) = 3,6,6
            # list(arr)의 값들은 tuple들로 되어있으모 join(map(str,))을 사용해 join해준다
            num = int(''.join(map(str, arr[j])))
            # num = 0,1,1,1,1,10,11,10,11,11,11,101,110,101,110
            if is_prime_number(num):
                # is_prime_number() 함수가 True일 경우 (= 소수일 경우) num 추가
                answer.append(num)

    # 같은 값이 나올 수 있기 때문에 set()을 통해 중복값 제거
    answer = list(set(answer))
    return len(answer)


print(solution("17"))       # result : 3
print(solution("011"))      # result : 2


# permutations 설명


def solution(numbers):
    answer = 0

    for i in range(1, len(numbers)+1):
        print(list(permutations(numbers, i)))
        # [('0',), ('1',), ('1',)]
        # [('0', '1'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '0'), ('1', '1')]
        # [('0', '1', '1'), ('0', '1', '1'), ('1', '0', '1'), ('1', '1', '0'), ('1', '0', '1'), ('1', '1', '0')]

    return answer
