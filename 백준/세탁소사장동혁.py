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
