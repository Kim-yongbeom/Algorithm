dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
num = int(input())
for i in range(3,num+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[num])