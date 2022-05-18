# 그래프에서 최단 경로를 구하는 “다익스트라(dijkstra) 알고리즘”
# 또는 모든 정점에서 모든 정점으로의 최단경로를 구하는 “플로이드 와샬(Floyd-Warshal) 알고리즘”을 사용하면 풀 수 있는 문제입니다.
# 다른 사람 풀이

import heapq

def solution(n, s, a, b, fares):
    answer = 0
    link = [[] for _ in range(n+1)]
    for x,y,z in fares:
        # 모든 방향의 요금을 저장
        link[x].append((z,y))
        link[y].append((z,x))
    
    def dijkstra(start):
        dist = [987654321] * (n+1)
        dist[start] = 0
        heap = []
        # 새로운 배열에 heappush를 하는거라
        # heapq.heapify(heap) 안해줘도됨
        # heapq.heapify(heap)는 원래 있는 리스트를 변경해주는거
        heapq.heappush(heap,(0,start))
        while heap:
            value, destination = heapq.heappop(heap)
            if dist[destination] < value:
                continue
            for v, d in link[destination]:
                next_value = value + v
                if dist[d] > next_value:
                    dist[d] = next_value
                    heapq.heappush(heap, (next_value, d))
        return dist
    
    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    # print(dp)
    answer = 987654321
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)
    
    return answer 

