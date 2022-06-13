N = int(input())
words = []
count = 0

for _ in range(N):
    words.append(input())

for i in words:
    group = []
    for j in range(len(i)):
        word = i[j]
        if word in group:
            if i[j-1] == word:
                group.append(word)
            elif i[j-1] != word:
                break
        else:
            group.append(word)
    if len(group) == len(i):
        count += 1

print(count)