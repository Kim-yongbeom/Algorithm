def solution(begin, target, words):

    answer = 0
    target_word = ''

    for n, word in enumerate(words):
        score = 0

        if target not in words:
            answer = 0
            break

        if target == word:
            answer += 1
            break

        for i in range(len(word)):
            if begin[i] != word[i]:
                score += 1
            if score == 2:
                break

        if score == 1:
            answer += 1
            begin = word

            target_word = target.strip(word)
            if len(target_word) == 1:
                print(word)
                return answer + 1

    return answer
