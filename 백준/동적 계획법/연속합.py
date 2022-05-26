n = int(input())
num = list(map(int,input().split()))
score = 0
arr = [0 for _ in range(n)]
for i in range(n):
    if score < 0:
        score = 0
    score += num[i]
    arr[i] += score
print(max(arr))