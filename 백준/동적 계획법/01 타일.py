N = int(input())
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
# 5 = 8
# 11111 00111 10011 11001 11100 10000 00001 00100

# N이 1일때 arr[2]가 들어가지 않는것을 방지해 +2 를 해줌
arr = [0 for _ in range(N+2)]
arr[1] = 1
arr[2] = 2

for i in range(3,N+1):
    arr[i] = (arr[i-1] + arr[i-2])%15746
print(arr[N])


# 다른사람코드
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
num = int(input())
for i in range(3,num+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[num])