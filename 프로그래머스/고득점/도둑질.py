# 짝수 홀수 구분해서 sum1, sum2에 더해주기
# 문제점: 인덱스 문제(해결), sum에서 다시 빼줄때 작은값을 빼줘야함(해결)
# 최종 문제점: 돈만 최대면 된다. 2칸씩 집을 털 필요없음...
# [55, 1, 100, 10, 15, 70, 20]
# 기댓값 〉	225
# [55, 1, 100, 10, 15, 20, 70]
# 기댓값 〉	185
def solution(money):
    answer = 0
    sum1, sum2 = 0, 0
    sum_list = []
    for i in range(0, len(money), 2):
        j = i + 1  
        
        sum1 += money[i]
        sum_list.append(money[i])
        # money의 길이가 홀수
        if j == len(money):
            sum_list.sort(reverse=True)
            sum1 -= min(sum_list)
            j -= 1
        sum2 += money[j]
        if i == j:
            sum2 -= money[j]
    answer = max(sum1, sum2)
    return answer


# 다른사람 코드
def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])
    
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대
