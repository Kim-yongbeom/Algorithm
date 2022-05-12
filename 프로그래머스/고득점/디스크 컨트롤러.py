# 내코드 틀림
import heapq
def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    # 막힌 이유: 리스트 순서대로 작업시간을 뽑아냈지만 리스트의 순서를 다양하게 조합해서 
    # 작업시간을 구하는 방법을 모르겠음
    while jobs:
        tmp = 0
        start = heapq.heappop(jobs)
        time = start[1]
        next = start[1]
        for j in jobs:
            time += (next - j[0]) + j[1]
            next += j[1]
        
        tmp = time//3
        print(tmp)
            
    return answer

# 다른사람코드
import heapq
def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            # start와 now가 계속 바뀌면서 범위 안에 들어가는것들을 push
            if start < j[0] <= now:
                # 힙에 push를 할 때는 작업의 소요 시간 기준으로 최소힙이 만들어져야 하기 때문에 jobs의 요소를 그대로 넣지 않고 [작업의 소요 시간, 작업이 요청되는 시점]으로 요소의 앞 뒤를 바꿔서 넣어준다.
                heapq.heappush(heap,[j[1], j[0]])
        print(heap)
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        # 작업완료했지만 대기시간이 더 긴 경우 now를 계속 더해줘서 맞춰줌
        else:
            now += 1
    return int(answer / len(jobs))