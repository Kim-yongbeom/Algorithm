# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        arr_list = array[commands[i][0]-1:commands[i][1]]
        arr_list.sort()
        answer.append(arr_list[commands[i][2]-1])

    return answer

# 2022-02-21 푼 것!!
# 반복문 range 부분에 3을 때려넣으면 안됨!! len(commands)로 정확한 값 넣어주기 (문제 잘못 읽음)
# 이 코드는 .sort() 안됨 why

# 이유
# list.sort()은 list을 그 자리에서 정렬하고 목록 인덱스를 변경하고 None을 반환합니다.(모든 내부 작업은 동일).
# sorted()은 list뿐만 아니라 반복 가능한 모든 작업에 적용할 수 있습니다.
# 문자열, 튜플, 딕셔너리, 제너레이터 등 모든 요소가 포함된 반복 가능한 객체를 정렬하여 반환합니다.
# 따라서 list를 변경하려면 list.sort()를 사용하고, 새로운 정렬된 객체를 원하면 sorted()를 사용하면 됩니다.
# list의 경우에 list.sort()는 복사본을 만들 필요가 없으므로 sorted()보다 빠릅니다. 다른 이터레이터의 경우 선택의 여지가 없습니다. (sorted만 사용할 수 있기 때문)


def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        arr = array[commands[i][0]-1: commands[i][1]]
        arr = sorted(arr)
        answer.append(arr[commands[i][2]-1])
    return answer
