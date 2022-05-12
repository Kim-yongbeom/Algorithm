def solution(scoville, K):
    answer = 0
    # [1,1,1] K:10 일때 인덱스 에러
    # sum(scoville) > K 조건 추가로 해결
    # [1,1,1] K:4 일때 return -1로 넘어가버림
    # 시간초과
    while True:
        scoville.sort(reverse=True)
        num = 0
        
        if K > scoville[-1] and sum(scoville) > K:
            answer += 1
            num = scoville[-1] + (scoville[-2] * 2)
            if K <= scoville[-2]:
                for i in range(1):
                    scoville.pop()
            else:
                for i in range(2):
                    scoville.pop()
            scoville.append(num)
            
        elif answer == 0:
            return -1
        
        else:
            break
    return answer

# 다른 사람 코드
import heapq

def solution(q,k):
    heapq.heapify(q) # heap 자료구조 변경
    cnt = 0 # 섞는 횟수 지정
    
    while True:
        if len(q) == 1 and q[0] < k:
            return -1
        
        # 리스트 안의 최솟값을 빼줌
        a = heapq.heappop(q)
        if a < k:
            b = heapq.heappop(q)
            new = a + (b*2)
            print(q,1)
            # new의 숫자가 q의 리스트안에서 들어감(크기에 맞는 인덱스로)
            heapq.heappush(q, new)
            print(q,2)
            cnt += 1
        else:
            return cnt