# 내 코드 38.5점
def solution(brown, yellow):
    answer = []
    width = 0
    length = 1
    count = yellow  # 타일 갯수 계산
    while count > 2:
        if count % 2 == 0:
            length += 1
            count = yellow / length
            #  2 ->  3 -> 4 -> 5
            # 12 ->  8 -> 6 -> 4(4.8)
            if int(count*10) % 10 != 0 or length > count:
                # 소수이거나, 세로 길이가 더 길때 동작
                length -= 1
                break
        else:
            break
    while count > 3:
        if count % 3 == 0:
            length += 2
            count = yellow / length
            if int(count*10) % 10 != 0 or length > count:
                # 소수이거나, 세로 길이가 더 길때 동작
                length -= 2
                break
        else:
            break
    width = yellow // length
    answer.append(width + 2)
    answer.append(length + 2)
    return answer


# 다른 사람 코드
def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total
    for b in range(1, (total//2)+1):
        # 소수 판별
        if (total / b) % 1 == 0:            # total / b = a
            a = total / b
            if a >= b:                      # a >= b
                if (2*a + 2*b) - 4 == brown:  # 2*a + 2*b = brown + 4
                    return [a, b]

    return answer

# 다른 코드 2


def solution(brown, yellow):
    s = brown + yellow
    for i in range(s, 2, -1):
        print(i)
        if s % i == 0:
            a = s//i
            if yellow == (i-2)*(a-2):
                return[i, a]

    return answer
