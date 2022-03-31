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
