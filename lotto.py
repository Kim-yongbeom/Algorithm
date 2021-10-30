import sys
def solution(lottos, win_nums):
    score = [6,6,5,4,3,2,1]
    cnt = 0
    max = 0
    min = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    max = cnt + lottos.count(0)
    min = cnt
    answer = [score[max], score[min]]
    return answer

lottos = list(map(int,sys.stdin.readline().split()))
win_nums = list(map(int,sys.stdin.readline().split()))
solution(lottos,win_nums)