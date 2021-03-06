def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    # bridge_length 만큼의 리스트 만들어 주기
    # print(trucks_on_bridge)
    # 2일때 [0,0]
    # 빈 도로를 0으로 표시해줌
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
        # print(trucks_on_bridge)
        # [0, 7]
        # [7, 0]
        # [0, 4]
        # [4, 5]
        # [5, 0]
        # [0, 6]
        # [6]
        # []
    return answer

# 다른 코드
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
