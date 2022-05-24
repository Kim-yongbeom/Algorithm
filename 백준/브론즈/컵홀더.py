people = int(input())
cup = input()
score = 0

# count 함수 사용
count = cup.count('LL')

if count <= 1:
    score = len(cup)
else:
    # LL의 갯수에서 +1을 해줘야됨
    # LL은 두개의 단어이지만 컵홀더는 한개이기 때문
    score = len(cup) - count + 1
print(score)
