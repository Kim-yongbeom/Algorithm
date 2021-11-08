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


# 다른 코드
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
