# 내코드
# 5,6노드 값이 없음
# 최소값으로 가져오지 않음
# 진행중
def solution(n, edge):
    answer = 0
    dic = {}
    for i in range(n):
        dic[i+1] = 0
    edge.sort()
    # [[1, 2], [1, 3], [2, 4], [3, 2], [3, 6], [4, 3], [5, 2]]
    while edge:
        next_node = edge.pop(0)
        for i in range(len(edge)):
            if next_node[1] == edge[i][0]:
                dic[next_node[1]] += dic[next_node[0]]
                dic[next_node[1]] += 1
    print(dic)
    return answer

# 다른 사람 코드
from collections import deque
def solution(n, edge):
    answer = 0
    graph = {}
    visited = [0]*n
    for e in edge:
        graph[e[0]] = graph.get(e[0], []) + [e[1]]
        graph[e[1]] = graph.get(e[1], []) + [e[0]]
    # print(graph)
    # {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]}
    queue = deque()
    queue.append(1)
    visited[0] = 1
    while queue:
        nodes = len(queue)
        # print(queue)
        # deque([1])
        # deque([3, 2])
        # deque([6, 4, 5])
        for i in range(nodes):
            current = queue.popleft()
            for c in graph[current]:
                if visited[c-1] == 0:
                    visited[c-1] = 1
                    queue.append(c)
    return nodes
