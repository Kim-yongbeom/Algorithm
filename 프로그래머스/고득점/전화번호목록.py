# 내 코드
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        # i+1을 하게 되면 index범위에 안맞는다고 에러
        # i-1로 풀게 되면 뒤죽박죽.. sort해줘야 i-1로 풀수있음
        if phone_book[i][:len(phone_book[i-1])] == phone_book[i-1]:
            answer = False
            return answer
    return answer

# 다른 풀이 !


def solution(phone_book):
    answer = True
    # 1. ["119", "97674223", "1195524421"]
    # 2. ["12", "123", "1235", "567", "88"]
    phone_book.sort()
    # 1. ['119', '1195524421', '97674223']
    # 2. ['12', '123', '1235', '567', '88']
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):  # 없어도 되긴한다.
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


# 다른 풀이 !
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# zip 함수
# print(list(zip([1, 2, 3], (4, 5, 6), "abcd")))
# -> [[1, 4, 'a'], [2, 5, 'b'], [3, 6, 'c']]

# startswith는 꽤 직관적인 함수로 p2가 p1으로 '시작'되면 True 아니면 False를 반환한다.
# startswith 함수
# print("dfagd".startswith("abcd")) False
# print("abcde".startswith("abcd")) True
