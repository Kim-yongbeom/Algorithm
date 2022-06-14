N = int(input())

for _ in range(N):
    result = ''
    repeat, word = input().split()
    for i in word:
        result += (i*int(repeat))
    print(result)