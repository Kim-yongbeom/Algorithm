## 딕셔너리

### get()

```
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    answer = 0
    graph = {}
    for e in edge:
        graph[e[0]] = graph.get(e[0], []) + [e[1]]
        graph[e[1]] = graph.get(e[1], []) + [e[0]]
    print(graph)
    # {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]}
```
- get 메소드의 첫번째 값(e[0])이 graph 딕셔너리안에 키값과 같은지 조회하고 있다면 해당하는 키의 value값 return
- 만약 graph 딕셔너리에 없다면 get 메소드의 두번째 값([]) return
- ```graph[e[0]] = graph.get(e[0], []) + [e[1]]``` 와 같이 value가 리스트인 형태에서 리스트를 더해준다면 [e[1]]값이 value의 리스트안에 추가된다.
<hr>

### setdefault()

```
def solution(word):
    dic = {}
    for letter in word:
        dic.setdefault(letter, 0)
        dic[letter] += 1
    return dic
```
- 빈 dict에 추가해주기
- setdefault 함수는 첫번째 인자로 키(key)값, 두번째 인자로 기본값(default value).
<hr>

### defaultdict()
```from collections import defaultdict```
- 임포트 해줘야함
```
from collections import defaultdict

def solution(word):
    dic = defaultdict(int)
    for letter in word:
        dic[letter] += 1
    return dic
```
- setdefault와 다르게 자동으로 결과값 설정
- int를 넣어주면 0을 return함
- list, set도 가능






