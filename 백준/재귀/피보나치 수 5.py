#Fn = Fn-1 + Fn-2
def p(n):
    if n >= 2:
        n = p(n-1) + p(n-2)
        return n
    elif n == 1:
        return 1
    elif n == 0:
        return 0

print(p(int(input())))