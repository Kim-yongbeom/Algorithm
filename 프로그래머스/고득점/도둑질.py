# 짝수 홀수 구분해서 sum1, sum2에 더해주기
# 문제점: 인덱스 문제(해결), sum에서 다시 빼줄때 작은값을 빼줘야함(해결)
# 최종 문제점: 돈만 최대면 된다. 2칸씩 집을 털 필요없음...
# 	[55, 1, 100, 10, 15, 70, 20]
#   기댓값 〉	225
#   [55, 1, 100, 10, 15, 20, 70]
#   기댓값 〉	185
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
            sum_list.append(money[i])
            sum_list.sort(reverse=True)
            sum1 -= min(sum_list)
            j -= 1
        sum2 += money[j]
        if i == j:
            sum2 -= money[j]
    answer = max(sum1, sum2)
    return answer
