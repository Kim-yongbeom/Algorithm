# 효율성 테스트 탈락
def solution(info, query):
    answer = []
    
    for q in query:
        OX = False
        cnt = 0
        qsplit = q.split()
        q_score = int(qsplit.pop())
        for i in info:
            isplit = i.split()
            i_score = int(isplit.pop())
            if q_score <= i_score:
                for qs in qsplit:
                    if qs == 'and':
                        continue
                    if qs == '-' or qs in isplit:
                        OX = True
                    elif qs not in i:
                        OX = False
                        break
            else:
                continue
            if OX:
                cnt += 1
        answer.append(cnt)
    return answer

# 다른 사람 코드
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)      
    return answer