# My Templates.py

---------

> [toc]



## 알고리즘 문제 접근법

> 



### [Data Structure](https://github.com/Dinoryong/CS-academy/tree/main/Data%20Structures)

1. **배열** : 임의의 사이즈를 선언 (Heap, Queue, Binary Tree, Hashing 사용)
2. **스택** : 행 특정조건에 따라 push, pop 적용
3. **큐** : BFS를 통해 순서대로 접근할 때 적용
4. **연결리스트** : 배열 구현, 포인터 구현 2가지 방법 - 삽입,삭제가 많이 일어날 때 활용하기
5. **그래프** : 경우의 수, 연결 관계가 있을 때 적용
6. **해싱** : 데이터 수만큼 메모리에 생성할 수 없는 상황에 적용
7. **트리** : Heap과 BST(이진탐색)



### [Algorithm](https://github.com/Dinoryong/CS-academy/tree/main/Algorithm)

1. **★재귀(Recursion)** : 가장 많이 활용. 중요한 건 호출 횟수를 줄여야 함 (반복 조건, 종료 조건 체크)
2. **★BFS, DFS** : 2차원 배열에서 확장 시, 경우의 수를 탐색할 때 구조체(class)와 visited 체크를 사용함
3. **★정렬** : 퀵소트나 머지소트가 대표적이지만, 보통 퀵소트를 사용함
4. **★메모이제이션(memoization)** : 이전 결과가 또 사용될 때, 반복 작업을 안하도록 저장
5. **★이분탐색(Binary Search)** : logN으로 시간복잡도를 줄일 수 있는 간단하면서 핵심적인 알고리즘
6. **최소신장트리(MST)** : 사이클이 포함되지 않고 모든 정점이 연결된 트리에 사용 (크루스칼, 프림)
7. **최소공통조상(LCA)** : 경우의 수에서 조건이 겹치는 경우. 최단 경로 탐색시 공통인 경우가 많을 때 적용
8. **Disjoint-Set** : 서로소 집합. 인접한 집함의 모임으로 Tree의 일종이며 시간복잡도가 낮음
9. **분할 정복** : 머지 소트에 사용되며 범위를 나누어 확인할 때 사용
10. **트라이(Trie)** : 모든 String을 저장해나가며 비교하는 방법
11. **비트마스킹** : `|는 OR, &는 AND, ^는 XOR` <<를 통해 메모리를 절약할 수 있음



### 문제를 푸는 좋은 습관

1. 문제를 올바른 `순서`로 이해한다. 

- 읽기 : 시간,메모리 제한, 문제 전체를 `꼼꼼히!!`

- 이해하기 : 제공되는 정보(변수들) 정리, 예제 데이터에 대해 이해

- 파악하기 : 가능한 최대, 최소 정답에 맞는 데이터를 직접 생성, 키워드가 되는 단어들을 체크



2. `시간`과 `공간 복잡도`를 계산한다.



- 시간을 아끼기 : "짤 가치가 있는가?"

| 알고리즘                   | 시간 복잡도                   | 공간 복잡도 |
| -------------------------- | ----------------------------- | ----------- |
| BFS & DFS (w/ 인접 리스트) | O(V+E)                        | O(V+E)      |
| Dijkstra                   | O(E log E) or O(E log V)      | O(V+E)      |
| Quick Sort                 | 평균 O(N log N) , 최악 O(N^2) | O(V)        |
| Binary Search              | O(N log N)                    | O(N)        |



- Sort 시간복잡도

[![img](https://camo.githubusercontent.com/2e4f678a0643a726fee31d550f82c4f81de4134005ed3053601067749d3901b0/68747470733a2f2f676d6c776a64393430352e6769746875622e696f2f696d616765732f616c676f726974686d2d717569636b2d736f72742f736f72742d74696d652d636f6d706c65786974792e706e67)](https://camo.githubusercontent.com/2e4f678a0643a726fee31d550f82c4f81de4134005ed3053601067749d3901b0/68747470733a2f2f676d6c776a64393430352e6769746875622e696f2f696d616765732f616c676f726974686d2d717569636b2d736f72742f736f72742d74696d652d636f6d706c65786974792e706e67)



3. 코드를 효율적으로 `함수화`해서 구현한다.

```python
# 나쁜 예
First Time {
    20줄 짜리 알고리즘. (ei. 다익스트라)
}
Second Time {
    20줄 짜리 알고리즘.
}
Third Time {
    20줄 짜리 알고리즘.
}

# 좋은 예
Dijkstra(conditions){
    20줄 짜리 알고리즘.
}
First Time {
    Dijkstra(first_conditions)
}
Second Time {
    Dijkstra(second_conditions)
}
Third Time {
    Dijkstra(third_conditions)
}
```



4. 코딩 테스트에서 `부분 점수`를 챙긴다.



### etc 코딩테스트 준비를 위해...

- 실제 코딩 테스트에서는 제출 횟수 제한이 있을 수 있으니 주의해야 한다.

- 온라인 IDE 이용 시, 자동으로 소스코드가 공개 Public 상태로 온라인에 배포되어 부정행위로 간주될 수도 있으니 주의해야 한다. (ex. 리플릿, 파이썬 튜터, 온라인 GDB)

  => 소스코드가 공개 설정으로 되어 있는지 확인할 필요가 있다.

- 오프라인 코테의 경우, 지원한 회사에서 구체적으로 명시한 시험 방식을 미리 숙지하자.



------------

## [Pythonic Way](https://github.com/Dinoryong/CS-academy/blob/main/Algorithm/Pythonic%20Way.md)

> [파이썬 언어 레퍼런스](https://docs.python.org/ko/3/reference/index.html)
>
> [파이썬 구글 스타일 가이드](https://google.github.io/styleguide/pyguide.html)



### Unpacking

### List Comprehension

### Dictionary 잘 쓰기

### Sorting

### 문자열

### Combination/Permutation



### etc

#### sum

#### join

#### swap

#### for, while문 에서의 else

#### Enumerate

#### Counter



---------

## 최신 코테 분석

> [programmers_고득점kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)
>
> [leetcode_](https://leetcode.com/problemset/all/?listId=wpwgkgt)



### 필수 테크닉

- 정렬 Array
- 문자열 처리
- DP
- Dijkstra
- BFS & DFS
- 완전 탐색
- 이분 탐색



### 높은 난이도로 나오는 알고리즘

- 배열에서의 DP
- Tree에서의 DP
- 투 포인터
- 위상 정렬



### 자료구조

- HashMap
- Deque (Queue)
- Stack
- Priority Queue
- Dynamic Array



#### 코딩테스트 알고리즘 분류 전체

- 구현
- DFS
- BFS
- Two pointer
- Brute Force
- DP
- Tree DP
- 시뮬레이션
- Union Find
- String
- 자료구조 -> 우선순위 큐, 스택, 트리
- 순열조합
- Trie
- Flood fill
- Bit masking
- 위상정렬
- 이분탐색
- 최단거리
- 파싱
- Segment Tree



#### 코딩테스트 자료구조 전체

- map
- set
- tree
- priority queue
- queue
- stack
- deque
- list



------------------

## 기업 별 특징

> 라인, 네이버, 카카오,



### 라인 LINE

> ㄹ



#### 2020 하반기 기출 분석

|      |                    |
| ---- | ------------------ |
| 2    | 시뮬레이션         |
| 2    | Deque              |
| 2    | 완전탐색 (n!)      |
| 1    | 관찰, 구현, Ad-hoc |
| 3    | 구현, 시뮬레이션   |



#### 2019 상반기 기출 분석

[2019 상반기 LINE 인턴 코테](https://deepwelloper.tistory.com/118)

|      |      |
| ---- | ---- |
|      | 구현 |
|      | BFS  |
|      | DFS  |
|      | DP   |



### 카카오 KAKAO

> 국내 코테 TOP level

- 문자열 관련 문제가 항상 나온다
- 백트래킹을 통한 완전 탐색을 중요시
- 지원자의 수준의 상한선을 다른 기업들보다 훨씬 높은 곳까지 파악하려고 한다.
- 그럼에도 불구하고 학부 수준의 자료구조, 알고리즘 지식을 벗어나는 경우는 없게 내려고 노력



#### 2020 기출 분석

|                                                              |      | [KAKAO blind recruitment 2020](https://programmers.co.kr/learn/challenges?tab=all_challenges) |
| ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
| [문자열 압축](https://programmers.co.kr/learn/courses/30/lessons/60057) | 1    | 문자열, (일종의) 투 포인터                                   |
| [자물쇠와 열쇠](https://programmers.co.kr/learn/courses/30/lessons/60059) | 2    | 구현 (배열 돌리기)                                           |
| [기둥과 보 설치](https://programmers.co.kr/learn/courses/30/lessons/60061) | 4    | 시뮬레이션, bfs                                              |
| [블록 이동하기](https://programmers.co.kr/learn/courses/30/lessons/60063) | 5    | bfs                                                          |
| [괄호 변환](https://programmers.co.kr/learn/courses/30/lessons/60058) | 2    | 올바른 괄호 문자열 판단, 재귀 호출                           |
| [가사 검색](https://programmers.co.kr/learn/courses/30/lessons/60060) | 4    | Trie, 정렬 + 이분탐색                                        |
| [외벽 점검](https://programmers.co.kr/learn/courses/30/lessons/60062) | 4    | 완전탐색 (nPr)                                               |



#### 2021 기출 분석

|                                                              |      | [KAKAO blind recruitment 2021](https://programmers.co.kr/learn/challenges?tab=all_challenges) |
| ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
| [신규 아이디 추천](https://programmers.co.kr/learn/courses/30/lessons/72410) | 1    | 문자열                                                       |
| [순위 검색](https://programmers.co.kr/learn/courses/30/lessons/72412) | 2    | 완전탐색(2^n), 정렬, 해쉬맵                                  |
| [광고 삽입](https://programmers.co.kr/learn/courses/30/lessons/72414) | 3    | 완전탐색(2^n), 정렬, 이분탐색, 인코딩                        |
| [매출 하락 최소화](https://programmers.co.kr/learn/courses/30/lessons/72416) | 2.5  | 최단거리                                                     |
| [메뉴 리뉴얼](https://programmers.co.kr/learn/courses/30/lessons/72411) | 4    | prefix sum of prefix sum, 투 포인터, 문자열 핸들링           |
| [합승 택시 요금](https://programmers.co.kr/learn/courses/30/lessons/72413) | 4    | 백트래킹(dfs) + 최단거리(bfs), 꽤 많은 구현량                |
| [카드 짝 맞추기](https://programmers.co.kr/learn/courses/30/lessons/72415) | 5    | 트리 dp                                                      |



-------------



#### refs

> [gyoogle_github](https://github.com/CS-box/tech-interview-for-developer/tree/master/Algorithm)
>
> [rhs0266_github](https://github.com/Algorithm-box/FastCampus/tree/main/%EA%B0%95%EC%9D%98%20%EC%9E%90%EB%A3%8C/01-%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%A4%80%EB%B9%84)
>
> [VSFe_github](https://github.com/Algorithm-box/Algorithm_Study/blob/main/Concept/00_Special/Pythonic_Code_For_Coding_Test.md)
>
> [pythonic_way_programmers](https://programmers.co.kr/learn/courses/4008)
>
> [ndb_youtube](https://youtu.be/m-9pAwq1o3w)
>
> [이것이 취업을 위한 코딩테스트다](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791162243077&orderClick=LEa&Kc=)
>
> [파이썬 알고리즘 인터뷰_book](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791189909178&orderClick=LAG&Kc=)
>
> [코딩 인터뷰 퀘스천_book](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9788931447842&orderClick=LAG&Kc=)





