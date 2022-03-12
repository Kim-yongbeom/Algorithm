# 진행중
def solution(brown, yellow):
    answer = []
    count = 1
    while yellow > 2:
        yellow = yellow // count
        if yellow % 2 == 0:
            count += 1
    print(count)
    length = count + 2

    return answer
