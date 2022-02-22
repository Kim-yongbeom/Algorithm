# 파이썬의 자체적인 정렬알고리즘을 사용하면 앞의 숫자부터 차례로 비교하며 정렬해주니,
# 인수값이 1000 이하이므로 문자 * 3 을 통해 3자리수 만들어줌.
# 길이를 3 곱한 원소들(3, 34, 32의 경우 333, 343434, 323232)를 정렬하면 343434 - 333 - 323232 순서로 정렬이됩니다.

def solution(numbers):
    answer = ''
    # 한줄 반복문을 통해 모든 원소들의 길이를 3 곱하여 새 배열 생성
    numbers2 = [str(n)*3 for n in numbers]

    # enumerate는 “열거하다”라는 뜻입니다.
    # 이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.
    # 보통 enumerate 함수는 for문과 함께 자주 사용됩니다.
    numbers3 = list(enumerate(numbers2))  # 각 원소에 enumerate 함수로 인덱스 붙여줌
    numbers3.sort(key=lambda x: x[1], reverse=True)  # 원소들의 값에 따라 정렬
    for index, value in numbers3:  # 정렬된 인덱스를 이용해 차례대로 answer 만들기
        answer += str(numbers[index])

    return str(int(answer))  # '0000' -> 0 같은 경우를 위하여 int로 한번 바꿔주고 다시 str으로!


# 다른코드
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # ''.join(리스트)
    # ''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.

    # '구분자'.join(리스트)
    # '구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
    # '_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

    return str(int(''.join(numbers)))
