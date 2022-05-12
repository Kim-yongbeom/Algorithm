# N이 i 개 만큼 있는 set을 만들어 준다.
# dp[1] 일 경우, {5} , dp[2] 일 경우 {5+5, 5-5, 5//5, 5*5}이기 때문에 이전(dp[1])의 구성요소의 사칙 연산 결과로 구성 되어있다.
# 이처럼 dp[3]을 해보면, 555 , (dp[1] 연산 dp[2]) , (dp[2] 연산 dp[1])이 되는것을 볼 수 있다.
# 만들어진 dp[i] set 에서 number이 존재하면 i를 반환.
# 끝까지 발견 못하면 -1을 출력
def solution(N, number):
    answer = -1
    dp = []
    
    for i in range (1,9): 
        # i = N의 개수
        all_case = set()
        check_number = int(str(N)* i)
        # {N}, {NN} , {NNN}...
        all_case.add(check_number)
        # print(dp)
        # []
        # [{5}]
        # [{5}, {0, 1, 10, 55, 25}]
        # [{5}, {0, 1, 10, 55, 25}, {0, 2, 4, 5, 6, 555, -20, -4, -50, 15, 11, 50, 275, 20, -5, 60, 125, 30}]
        for j in range(0,i-1):      
            # j 개를 사용해서 만든 값들
            for op1 in dp[j]:
                # op1, op2를 번갈아가며 계산
                for op2 in dp[-j-1]:
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
                        
        if number in all_case:
            answer = i
            break
            
        dp.append(all_case) 
        

    return answer