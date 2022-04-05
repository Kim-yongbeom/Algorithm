# 다른 사람 코드
def solution(n, results):
    answer = 0
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    for i, j in results:
        win[i].append(j)
        lose[j].append(i)
    # print(win)
    # [[], [2], [5], [2], [3, 2], []]
    # print(lose)
    # [[], [], [4, 3, 1], [4], [], [2]]
    for i in range(1, n+1):
        for w in win[i]:
            if lose[i]:
                for l in lose[i]:
                    if l not in lose[w]:
                        lose[w].append(l)
                    if w not in win[l]:
                        win[l].append(w)
    # print(win)
    # [[], [2, 5], [5], [2, 5], [3, 2, 5], []]
    # print(lose)
    # [[], [], [4, 3, 1], [4], [], [2, 4, 3, 1]]
    for w, l in zip(win, lose):
        if len(w)+len(l) == n-1:
            answer += 1
    return answer
