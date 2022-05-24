N = int(input())
mountains = list(map(int,input().split()))
ans = 0
cnt = 0
max_mountain = 0
for mountain in mountains:
    if mountain > max_mountain:
        cnt = 0
        max_mountain = mountain
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)
