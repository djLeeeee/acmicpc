[![Solved.ac Profile](https://camo.githubusercontent.com/a61cd4a3f0ec198a2b27d7f242c3387bd80d58e437ddaca71f4c2bef052c5e7e/68747470733a2f2f6d617a617373756d6e6964612e7774662f6170692f76322f67656e65726174655f62616467653f626f6a3d626f6d756c31313238)](https://solved.ac/bomul1128)

# 백준 온라인 문제풀이

- 다른 문제 풀 때 다시 쓸만한 코드 / 재밌게 짠 코드만 올릴 것!

## 1. 시간복잡도

https://wiki.python.org/moin/TimeComplexity

1. list : LIFO 에 좋음
   - O(1) : `append` `pop` `len` my_list[1] = 3 (set data) ....
   - O(n): `popleft` `delete` `in` `insert`
   - O(nlogn) : `sort` => 웬만한 sort는 다 이걸로 사용하자
2. set
   - O(1) : `in`
   - O(n) : `update`(추가하려는 list의 길이에 비례)

큐, 덱, 딕셔너리...

## 0207
- 플로이드 와샬 : [11403_경로찾기](https://www.acmicpc.net/problem/11403)
시작점과 끝점을 잇는 길이 1의 간선들의 정보가 주어졌을 때 활용할 수 있다. 삼중 for문으로 구성되며 코드는 굉장히 간단했다.(코드 참고) for i / for j / for k의 구조에서 i는 경로 중간의 노드, j는 시작점, k는 끝점을 의미한다. 당연히 j k 순서는 바뀌어도 된다. 핵심은 i번째 제일 바깥 반복문이 돌 때, 0~i의 노드를 지나 연결되는 두 노드 들의 정보가 갱신된다는 것이다.
플로이드 와샬은 노드의 갯수를 v라고 했을 때 시간 복잡도는 O(v^3)이다. 해당 문제는 각각의 노드에 대해서 bfs 탐색을 진행해도 풀 수 있다. 그랬을 때 시간복잡도는 아마 O(v^2)이다. 11403번 같이 간선에 비중이 없는 경우엔, 플로이드 와샬을 쓸 필요가 없다! 그냥 이럴 땐 bfs 탐색 쓰자.

- find-union : [6091_핑크플로이드](https://www.acmicpc.net/problem/6091)
코드 자체는 간단하다. 속해있는 집합의 대표 원소를 찾는 find 함수와 두 원소가 속한 각각의 집합을 합치는 union 함수 2개를 만들면 끝. 처음에 할 땐 이것을 어디다 쓰나 싶었는데, 어제 푼 15586 무튜브 문제같이 원소와 원소간에 연결되어 있는지 확인할 때 bfs / dfs 보다 훨씬 편리한 것 같다.
파이썬으로 하다보니 find 함수의 재귀 부분에서 오래 걸릴 때가 있다. find-union의 상위 호환 개념도 있을지도?

## 0208