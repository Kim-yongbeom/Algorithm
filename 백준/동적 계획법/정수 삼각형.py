n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n-2,-1,-1):
    for j in range(len(l[i])):
        l[i][j] += max(l[i+1][j], l[i+1][j+1])
print(l[0][0])