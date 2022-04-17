# 내 코드
# 33점..
# 좌우 방향키를 어떻게 설정해줄지 모르겠음
# A를 기준으로 해줘야하는거같음
def solution(name):
    answer = 0
    word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in name:
        if word.index(i) > len(word)//2:
            answer += (len(word) - word.index(i))
        else:
            answer += word.index(i)
    if 'A' in name:
        answer -= 1
    return answer + len(name)-1

# 다른 사람 코드


def solution(name):

    # 조이스틱 조작 횟수
    answer = 0

    # word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가

        # min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) 와 밑의 코드는 똑같다

        # if word.index(char) > len(word)//2:
        #     answer += (len(word) - word.index(char))
        # else:
        #     answer += word.index(char)
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        # ord(문자)
        # 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # ex) JAAJAAAAJ 인 경우 4번째 J를 처리하기 위해서 2, 3번째의 연속된 AA를 건너는게 5,6,7,8번쨰의 연속된 AAAA를 건너는 것 보다 낫다.
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) -
                       next, i + 2 * (len(name) - next)])
    
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer
