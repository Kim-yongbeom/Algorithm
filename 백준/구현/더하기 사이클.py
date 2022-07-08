N = int(input())
cnt = 1

w1 = N // 10
w2 = N % 10
sum_w = w1 + w2
new_w = (w2*10) + (sum_w%10)

while True:
    if N == new_w:
        break
    w1 = new_w // 10
    w2 = new_w % 10
    sum_w = w1 + w2
    new_w = (w2*10) + (sum_w%10)
    cnt += 1

print(cnt)