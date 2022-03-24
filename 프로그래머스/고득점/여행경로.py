# 50점
# 문제 2개 런타임 에러
def solution(tickets):
    answer = ["ICN"]
    V = [0 for i in range(len(tickets))]
    
    # 항상 ICN에서 출발
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            start, target = tickets[i]
    
    for _ in range(len(tickets)):
        same = []
        for i, ticket in enumerate(tickets):
            if not V[i]:
                if start == ticket[0]:
                    same.append([ticket[1], i])
                    same = sorted(same)
                    target = same[0][0]
        if target == same[0][0]:
            V[same[0][1]] = 1
            answer.append(target)
            start = target
        
    return answer

# 다른 사람 코드
