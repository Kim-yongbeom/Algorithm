num_list = list(map(str, input().split()))
min1 = ''
min2 = ''
max1 = ''
max2 = ''
for i in range(len(num_list[0])):
    if num_list[0][i] == '5':
        min1 += '5'
        max1 += '6'
    elif num_list[0][i] == '6':
        min1 += '5'
        max1 += '6'
    else:
        min1 += num_list[0][i]
        max1 += num_list[0][i]

for i in range(len(num_list[1])):
    if num_list[1][i] == '5':
        min2 += '5'
        max2 += '6'
    elif num_list[1][i] == '6':
        min2 += '5'
        max2 += '6'
    else:
        min2 += num_list[1][i]
        max2 += num_list[1][i]
max1 = int(max1)
max2 = int(max2)
min1 = int(min1)
min2 = int(min2)
score1 = min1 + min2
score2 = max1 + max2
print(score1, score2)
