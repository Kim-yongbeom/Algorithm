from collections import Counter


def solution(N, stages):
    answer = []
    score = []
    stages.sort(reverse=True)
    count = Counter(stages)
    for n in range(1, N+1):
        if count[n] != 0:
            score.append([n, count[n]/len(stages)])
        elif count[n] == 0:
            score.append([n, 0])
        if stages:
            for _ in range(count[n]):
                stages.pop()
    score.sort(key=lambda x: x[1], reverse=True)
    for i in score:
        answer.append(i[0])
    return answer
