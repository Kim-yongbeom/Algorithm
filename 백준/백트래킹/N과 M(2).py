# 내코드
n,m = list(map(int,input().split()))
 
s = []
boolean = False
 
def dfs():
    if len(s)==m:
        if len(s) == 1:
            print(' '.join(map(str,s)))
            return
                    
        else:
            for a in range(len(s)-1):
                if s[a] < s[a+1]:
                    boolean = True
                else:
                    boolean = False
                    break
                    
        if boolean:
            print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()


# 다른사람코드
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)