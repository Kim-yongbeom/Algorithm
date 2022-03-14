# BFS를 이용한 풀이
# numbers의 숫자를 더하거나 뺀 경우를 수평적으로 추가해준다.
# 결국 leaves리스트에 모든 계산 결과가 담기게 된다. 이후 target값과 비교해서 결과 출력.

def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer


# DFS를 이용한 풀이
# BFS가 수평적으로 더해 한꺼번에 모든 결과값을 얻었다면, DFS를 이용할 땐 하나씩 비교한다
# depth 변수 값을 통해 탐색 중인 트리의 깊이를 알 수 있다.
# 트리 끝에 도착했다면, number값을 모두 더한 값을 비교한다.

def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer


def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer
