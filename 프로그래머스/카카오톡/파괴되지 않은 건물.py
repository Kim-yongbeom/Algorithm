# 다른 사람 코드
# https://kimjingo.tistory.com/155
def solution(board, skill):
    answer = 0
    # 누적합 기록을 위한 배열
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)] 

    for type, r1, c1, r2, c2, degree in skill:
        # 누적합 기록, 부호에 주의할 것
        if type == 2: 
            tmp[r1][c1] += degree 
        else: 
            tmp[r1][c1] -= degree
        # 위 코드와 같은 형태 
        if type == 2: 
            tmp[r1][c2 + 1] += -degree
            # 이렇게 해도 됨
            # tmp[r1][c2 + 1] -= degree
        else: 
            tmp[r1][c2 + 1] += degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree 
    # print(tmp)
    # [[-4, -1, 0, 0, 1, 4], [2, 0, -2, 0, 0, 0], [-2, 0, 0, 0, 2, 0], [2, 0, 0, 0, -2, 0], [2, 1, 2, 0, -1, -4]]
    # 행 기준 누적합
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]
    # 열 기준 누적합
    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]
    # 기존 배열과 합함
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1
    return answer