def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

# 다른 풀이


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


zip 함수
print(list(zip([1, 2, 3], (4, 5, 6), "abcd")))
-> [[1, 4, 'a'], [2, 5, 'b'], [3, 6, 'c']]

startswith는 꽤 직관적인 함수로 p2가 p1으로 시작되면 True 아니면 False를 반환한다.
startswith 함수
print("dfagd".startswith("abcd")) False
print("abcde".startswith("abcd")) True
