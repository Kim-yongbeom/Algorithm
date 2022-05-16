def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i in new_id:
        # isalnum -> 영어, 한글, 숫자면 true 아니면 false
        if i.isalnum() or i in '-_.':
            answer += i
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..','.')
    
    # 4단계
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if len(answer) == 0:
        answer += 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer