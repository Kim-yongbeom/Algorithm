m = int(input())
a = 0
b = 0
c = 0

while True:
    if m >= 300:
        a += 1
        m -= 300
    elif m >= 60:
        b += 1
        m -= 60
    elif m >= 10:
        c += 1
        m -= 10
    # 10보다 작고 실수 -> -1
    elif m >= 1:
        print(-1)
        break
    # 10보다 클 경우에서 -10을 해주므로 음수가 나올 경우, 0이 나올 경우 break
    else:
        print(a, b, c)
        break
