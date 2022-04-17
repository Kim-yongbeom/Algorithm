def solution(clothes):
    # [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    closet = {}
    result = 1
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)
            # print(closet[key]), key = headgear
            # ['yellow_hat', 'green_turban'] 같은 종류값 나옴
        else:
            closet[key] = [value]
            # print(closet[key])
            # ['yellow_hat']
            # ['blue_sunglasses']

    # -1은 x+1 (안입은 경우 포함) 을 하면서 곱해나가기 때문에 결과에 하나도 안입은 경우가 포함되어서 그 경우를 빼주기 위해 사용
    for key in closet.keys():
        result = result * (len(closet[key]) + 1)
    return result - 1


# 다른 사람 코드
def solution(clothes):
    # [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = 1
    dic = dict()

    # kind = clothes의 종류가 나온다
    # [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]] 에서 headgear, eyewear, headgear 
    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1

    for val in dic.values():
        answer *= (val + 1)

    return answer - 1
