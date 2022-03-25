# 내 코드
# 실패
def solution(progresses, speeds):
    answer = []
    score = []
    time = 0
    while True:
        for i in range(len(progresses)):
            if len(score) < len(progresses):
                score.append(progresses[i]+speeds[i])
            else:
                score[i] += speeds[i]
        time += 1
        print(score)
        break

    return answer
