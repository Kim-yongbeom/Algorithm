n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
#             print(s,1)
            dfs()
            
#             print(s,2)
            s.pop()
#             print(s,3)
dfs()