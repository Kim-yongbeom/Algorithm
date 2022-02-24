# 역정렬하고 citations[i] <= i+1 인거 아닌가...?
# 틀림 (내 코드)
def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i+1:
            answer = i+1
            break
    return answer

# 내 코드
# i+1 에서 +1 삭제하면 한개빼고 다 성공
# 왜 논문의 수는 1편~1000편인데 인덱스는 0 부터 시작할까 1부터 시작해야 하는거 아닌가??
# citations     	return
# [3, 0, 6, 1, 5]	3

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        # print(i) 를 넣을 경우 0,1,2,3 이 출력된다
        # print(citations[i]) 를 넣을 경우 6,5,3,1 이 출력된다
        if citations[i] <= i:
            answer = i
            break
    return answer

# 다른 사람 풀이
# 왜 위에 코드는 안될까 ????

def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        # print(idx) 를 넣을 경우 0,1,2,3 이 출력된다
        # print(citation) 을 넣을 경우 6,5,3,1 이 출력된다
        if idx >= citation:
            return idx
    # 만약 return len(citations)를 삭제하면  위 코드와 똑같이 테스트 9번만 틀리는 현상 발견!!
    return len(citations)


# 주석대로 반복문 밖의 return값 바꿔보기
# 성공함
# 테스트 9번은 뭘까..?

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            answer = i
            return answer
    return len(citations)

# 원인

# 인용 리스트에 있는 가장 큰 수부터 가장 작은 수까지 내려가면서 iteration을 했는데,

# 인용 리스트에 있는 가장 큰 수부터 가장 작은 수까지가 아니라, 0까지 iteration을 돌렸어야했다.

# 예제에 나온 테스트케이스에는 항상 0이 포함되어있어서 실수를했다.

# citations = [10, 50, 100] 으로 테스트를 해 보면 무슨말인지 알 것이다.

# 참고로 이 경우 H-INDEX는 3이 나와야한다.

# 그러므로 0이 없는 리스트를 위해 return len(citations) 해줘야함

# 다른 느낌의 코드
def solution(citations):
    citations.sort(reverse = True)
    answer = []
    for i, d in enumerate(citations, start=1) :
        # i, d중 더 작은것 추가
        answer.append(min(i,d))
    return max(answer)
