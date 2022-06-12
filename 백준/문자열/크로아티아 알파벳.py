N = input()
count = 0
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in a:
    N = N.replace(i,'_')
        
print(len(N))