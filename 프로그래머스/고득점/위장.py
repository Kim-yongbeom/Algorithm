def solution(clothes):
    closet = {}
    result = 1
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    # -1은 x+1 (안입은 경우 포함) 을 하면서 곱해나가기 때문에 결과에 하나도 안입은 경우가 포함되어서 그 경우를 빼주기 위해 사용
    for key in closet.keys():
        result = result * (len(closet[key]) + 1)
    return result - 1
