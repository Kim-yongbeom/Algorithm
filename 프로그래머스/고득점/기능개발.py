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

# 다른 사람코드


def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
