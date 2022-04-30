# 알고리즘

## 자주 나오는 유형!!
https://velog.io/@shininghyunho/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%BD%94%ED%85%8C%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%95%EB%A6%AC

## 컴파일 타임
```
개발자에 의해 C, JAVA 등과 같은 개발 언어로 소스코드가 작성되며, 
컴파일 과정을 통해 컴퓨터가 인식할 수 있는 기계어 코드로 변환되어 
실행 가능한 프로그램이 되는 과정을 의미한다.
```
## 런타임 에러
```
이미 컴파일이 완료되어 프로그램이 실행중임에도 불구하고, 
의도치 않은 예외 상황으로 인하여 프로그램 실행 중에 발생하는 오류 형태를 의미한다.
```
- 배열에 할당된 크기를 넘어서 접근했을 때
- 전역 배열의 크기가 메모리 제한을 초과할 때
- 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
- 0으로 나눌 떄
- 라이브러리에서 예외를 발생시켰을 때
- 재귀 호출이 너무 깊어질 때
- 이미 해제된 메모리를 또 참조할 때

## DFS(깊이우선탐색)
- 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색
- 스택 또는 재귀함수로 구현

## BFS(너비우선탐색)
- 현재 정점에 연결된 가까운 점들부터 탐색
- 큐를 이용해서 구현
```
데크(deque)의 개념
보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 반면, 양방향 큐가 있는데 그것이 바로 데크(deque)다.

즉, 앞, 뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.

데크는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.

컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 
일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 데크(deque)는 O(1)로 접근 가능하다.
```
- deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
- deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
- deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- deque.remove(item): item을 데크에서 찾아 삭제한다.
- deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

## 이진 탐색(이분 탐색) 
- 알고리즘은 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법이다.
- 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
- 변수 3개(start, end, mid)를 사용하여 탐색한다. 
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것이 이진 탐색의 과정이다.

## 그리디 알고리즘
- 그리디 알고리즘은 탐욕 알고리즘 또는 욕심쟁이 알고리즘이다.
- 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법이다. 
- 이렇게 각 단계에서 최선의 선택을 한 것이 전체적으로도 최선이길 바라는 알고리즘이다.

## Kruskal 알고리즘
- 탐욕적인 방법(greedy method) 을 이용하여 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것이다.

