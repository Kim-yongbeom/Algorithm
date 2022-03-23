def solution(begin, target, words):

    answer = 0
    target_word = ''

    for n, word in enumerate(words):
        score = 0

        if target not in words:
            answer = 0
            break

        for i in range(len(word)):
            if begin[i] != word[i]:
                score += 1
            if score >= 2:
                break

        if score == 1:
            # 알파벳이 하나 차이나는것 중에서 target과 word 같으면 answer + 1
            # 밑에서의 target_word와 차이점은
            # 첫번째의 word가 target이랑 같다면 실행이 안되기 때문에
            # 이 조건문을 걸어줌
            if target == word:
                return answer + 1
            answer += 1
            begin = word

            # target 단어에서 word의 알파벳 전부 삭제
            target_word = target.strip(word)
            if len(target_word) == 1:
                print(word)
                return answer + 1

    return answer

# 다른사람 코드
from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [ 0 for i in range(len(words))]
    while q:
        print(q)
        word, cnt = q.popleft()
        
        print(word, cnt)
        
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    # 이미 append된 단어는 V = 1 처리
                    V[i] = 1
                    
    return answer
