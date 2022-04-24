# 내 코드
def solution(number, k):
    answer = ''
    num_list = [0]
    k += 1
    for num in number:
        num = int(num)
        # num_list 조건을 앞에 써줘야함
        while num_list and num_list[-1] < num and k > 0:
            k -= 1
            num_list.pop()
        num_list.append(num)
    # 같은 숫자 반복이여서 k를 다 쓰지 않았는데 반복문이 끝낫을때
    if k:
        for i in range(k):
            num_list.pop()
    
    for num in num_list:
        num = str(num)
        answer += num

    # 앞자리가 0일때를 생각
    return str(int(answer))

# 다른 사람 코드


def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])
