def solution(new_id):
    answer = ''
    
    # lower() : 소문자 바꿔주기
    new_id = new_id.lower()
    
    # isalnum() : 숫자
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
    
    # replace() : 교체
    while '..' in answer:
        answer = answer.replace('..','.')
        
    # answer and 를 해주지 않으면 런타임 에러 발생 -> 원소가 있는지 확인해야 하나봄
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    if len(answer) == 0:
        answer += 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer