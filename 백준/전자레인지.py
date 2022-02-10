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
    elif m >= 1:
        print(-1)
        break
    else:
        print(a, b, c)
        break
