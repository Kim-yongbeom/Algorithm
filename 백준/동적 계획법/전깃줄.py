N = int(input())

lineList = []

for _ in range(N):
    lineList.append(list(map(int, input().split())))

lineList.sort()


dp = [1]*N
for i in range(N):
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
# 없애야 하는 전깃줄의 최소 개수 = 현재 전깃줄의 개수 - 겹치치 않는 최대 전깃줄의 개수
print(N-max(dp))