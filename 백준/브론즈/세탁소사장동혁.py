# 다른사람코드
# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     q, d, n, p = 0, 0, 0, 0
#     t = int(input())
#     q = t//25
#     t = t%25
#     d = t//10
#     t = t%10
#     n = t//5
#     t = t%5
#     p = t

#     print(q, d, n, p)
    
T = int(input())

for i in range(T):
    Q = 0
    D = 0
    N = 0
    P = 0
    num = int(input())
    while num > 0:
        if num >= 25:
            num -= 25
            Q += 1
        elif num >= 10:
            num -= 10
            D += 1
        elif num >= 5:
            num -= 5
            N += 1
        elif num >= 1:
            num -= 1
            P += 1
    print(Q, D, N, P)
