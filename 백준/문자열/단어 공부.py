from collections import Counter
word = input().upper()
count = 0
max_count = max(Counter(word).values())

for i, j in Counter(word).items():
    if max_count == j:
        count += 1
        a = i
    if count > 1:
        print('?')
        break
if count == 1:
    print(a)