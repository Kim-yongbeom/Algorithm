# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    basket = [0]
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if board[j][i-1] != basket[-1]:
                    basket.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
                elif board[j][i-1] == basket[-1]:
                    board[j][i-1] = 0
                    basket.pop()
                    answer += 2
                    break
    return answer
