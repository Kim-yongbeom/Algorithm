# 다른 사람 코드
def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key=lambda x: x[2])  # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]])  # 집합
    # print(costs)
    # [[0, 1, 1], [1, 3, 1], [0, 2, 2], [1, 2, 5], [2, 3, 8]]
    # [[3, 1, 2], [1, 2, 3], [2, 3, 3], [3, 0, 4], [0, 1, 5], [2, 4, 6], [4, 0, 7]]
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                print(routes)
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans
