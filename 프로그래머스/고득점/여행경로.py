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
def solution(tickets):
    
    routes = dict()
    for i in tickets:
        if i[0] in routes:
            routes[i[0]].append(i[1])
        else:
            routes[i[0]] = [i[1]]
    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    # print(routes)
    for i in routes.keys():
        routes[i].sort(reverse = True)
    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}
    # print(routes)
    answer = []
    start = ["ICN"]
    
    while start:
        # ['ICN']
        # ['ICN', 'ATL']
        # ['ICN', 'ATL', 'ICN']
        # ['ICN', 'ATL', 'ICN', 'SFO']
        # ['ICN', 'ATL', 'ICN', 'SFO', 'ATL']
        # ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']
        # ['ICN', 'ATL', 'ICN', 'SFO', 'ATL']
        # ['ICN', 'ATL', 'ICN', 'SFO']
        # ['ICN', 'ATL', 'ICN']
        # ['ICN', 'ATL']
        # ['ICN']
        # print(start)
        target = start[-1]
        if target not in routes or len(routes[target]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[target].pop())
    # ['SFO', 'ATL', 'SFO', 'ICN', 'ATL', 'ICN']
    # print(answer)
    return answer[::-1]
