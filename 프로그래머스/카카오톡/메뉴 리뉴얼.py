from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        # most_common() 최빈값 구하기
        sorted_candidates = Counter(candidates).most_common()
#         print(sorted_candidates)
#         ["XYZ", "XWY", "WXA"]
        
#         [('XY', 2), ('WX', 2), ('XZ', 1), ('YZ', 1), ('WY', 1), ('AW', 1), ('AX', 1)]
#         [('XYZ', 1), ('WXY', 1), ('AWX', 1)]
#         []
        
        # sorted_candidates[0][1] 왜 해주는걸까
        # cnt = sorted_candidates[0][1]는 3번째 문제 마지막이 빈배열이라?
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)