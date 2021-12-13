# https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3#
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# 다른사람 코드
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
