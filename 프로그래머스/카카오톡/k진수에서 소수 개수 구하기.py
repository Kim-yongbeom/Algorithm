def solution(n, k):
    rev_base = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n, k)
        # dicmod(a,b) = a//b, a%b
        rev_base += str(mod)
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    base = rev_base[::-1]
    base = base.split('0')
    
    sosu = True
    
    for b in base:
        if b == '':
            continue
        if int(b) < 2:
            continue
        else:
            for i in range(2, int(int(b)**0.5) + 1):
                if int(b) % i == 0:
                    sosu = False
                    break
            if sosu:
                answer += 1
    
    return answer