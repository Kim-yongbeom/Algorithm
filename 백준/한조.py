num = int(input())
mount = input()
score = 0
winner = map(int, mount.split(' '))

for i in range(num):
    if winner[i] > winner[i+1]:
        score += 1
    elif winner[i] < winner[i+1]:
        score = 0
