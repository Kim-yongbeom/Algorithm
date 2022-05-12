import heapq
def solution(operations):
    answer = []
    lists = []
    for i in operations:
        if i[0][0] == 'I':
            heapq.heappush(lists,int(i.split(' ')[1]))
        # lists 안넣어주면 런타임에러 발생!! lists의 원소가 없을때 실행되는걸 막아줌
        elif lists and i[0][0] == 'D':
            if i[2] == '-':
                heapq.heappop(lists)
            elif i[2] == '1':
                # 최소 힙에서 최대값 삭제하기
                # heapq.nlargest(n, list) 함수를 사용하면 list에서 
                # 가장 큰 n개의 수를 뽑아 낼 수 있다. 
                # 위 코드에서 heap의 원소 개수만큼 뽑아 내기 때문에 
                # heap 리스트는 내림 차순으로 정렬이 되어 있는 상태이다.
                # 이 상태에서 1부터 슬라이싱을 하면 가장 큰 최대값이 제외될 것이고, 
                # 다시 최소힙으로 만들어주면 된다.
                lists = heapq.nlargest(len(lists), lists)[1:]
                heapq.heapify(lists)
    if len(lists) == 0:
        for _ in range(2):
            answer.append(0)
    elif len(lists) == 1:
        answer.append(lists[0])
        answer.append(0)
    else:
        answer.append(max(lists))
        answer.append(min(lists))
            
    return answer