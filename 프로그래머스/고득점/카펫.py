# 진행중
def solution(brown, yellow):
    answer = []
    width = 0
    length = 1
    while yellow > 2:
        if yellow % 2 == 0:
            length += 1
            yellow = yellow // length
            # 24 -> 12 ->  4
            # 1  ->  2 ->  3
            # 오류 이유 : legnth를 계속 늘어날때 마다 나눠줘서 yellow값이 계속 작아짐
            # length 값을 계속 올린후 한번에 나눠줘야함
            if yellow % length != 0:
                length -= 1
                yellow = yellow * length
                break
    width = yellow
    print(width)

    answer.append(width + 2)
    answer.append(length + 2)
    return answer
