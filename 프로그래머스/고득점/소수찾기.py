def solution(numbers):
    answer = 0
    for idx, number in enumerate(numbers):
        number = int(number)
        if number % 2 != 0:
            print(1)
    return answer
