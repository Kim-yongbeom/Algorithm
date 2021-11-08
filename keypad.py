# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ""
    lastL = 10
    lastR = 12
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            lastL = i
        elif i in [3,6,9]:
            answer += 'R'
            lastR = i
        else:
            if i == 0:
                i = 11
            L_dis = abs(lastL-i)//3 + abs(lastL-i)%3
            R_dis = abs(lastR-i)//3 + abs(lastR-i)%3
            
            if L_dis > R_dis:
                answer += 'R'
                lastR = i
            elif R_dis > L_dis:
                answer += 'L'
                lastL = i
            else:
                if hand == 'right':
                    answer += 'R'
                    lastR = i
                else:
                    answer += 'L'
                    lastL = i
    return answer