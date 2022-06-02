# 내 코드
# 틀림 왜 틀렷는지 모르겟다..
A = int(input())
B = list(map(int,input().split()))
cnt = 0
max = 0
for i in B:
    num = i
    if num > max:
        max = num
        cnt += 1
print(cnt)

# 다른 사람 코드
N = int(input())
numbers = list(map(int, input().split()))
LIS = [1] * N
for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)

print(max(LIS))