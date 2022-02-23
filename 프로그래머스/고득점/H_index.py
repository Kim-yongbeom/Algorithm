# 역정렬하고 citations[i] <= i+1 인거 아닌가...?
# 틀림 (내 코드)
def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i+1:
            answer = i+1
            break
    return answer

# i+1 에서 +1 삭제하면 한개빼고 다 성공


def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            answer = i
            break
    return answer

# 다른 사람 풀이


def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)
