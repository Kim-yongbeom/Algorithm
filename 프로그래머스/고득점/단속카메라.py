# 내코드
# 틀림
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    # print(routes)
    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    n = routes[0][0]
    for route in routes:
        if n < route[0]:
            answer += 1
            n = route[1]
    return answer

# 다른 사람 코드


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    leng = len(routes)
    checked = [0] * leng

    for i in range(leng):
        if checked[i] == 0:
            camera = routes[i][1]  # 진출 지점에 카메라를 갱신
            answer += 1
        for j in range(i+1, leng):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    return answer

# 다른 사람 코드


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001  # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
