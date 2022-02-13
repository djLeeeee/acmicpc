[![Solved.ac Profile](https://camo.githubusercontent.com/a61cd4a3f0ec198a2b27d7f242c3387bd80d58e437ddaca71f4c2bef052c5e7e/68747470733a2f2f6d617a617373756d6e6964612e7774662f6170692f76322f67656e65726174655f62616467653f626f6a3d626f6d756c31313238)](https://solved.ac/bomul1128)


![image](https://user-images.githubusercontent.com/97663863/153756080-77b9523a-6942-4e57-bcbe-ac05e4123fe2.png)
22년 2월 13일 시작한지 한 달만에 플레 달성!




# 백준 온라인 문제풀이

- 다른 문제 풀 때 다시 쓸만한 코드 / 재밌게 짠 코드만 올릴 것!

  

## 0207
- 플로이드 와샬 : [11403_경로찾기](https://www.acmicpc.net/problem/11403)
  시작점과 끝점을 잇는 길이 1의 간선들의 정보가 주어졌을 때 활용할 수 있다. 삼중 for문으로 구성되며 코드는 굉장히 간단했다.(코드 참고) for i / for j / for k의 구조에서 i는 경로 중간의 노드, j는 시작점, k는 끝점을 의미한다. 당연히 j k 순서는 바뀌어도 된다. 핵심은 i번째 제일 바깥 반복문이 돌 때, 0~i의 노드를 지나 연결되는 두 노드 들의 정보가 갱신된다는 것이다.
  플로이드 와샬은 노드의 갯수를 v라고 했을 때 시간 복잡도는 O(v^3)이다. 해당 문제는 각각의 노드에 대해서 bfs 탐색을 진행해도 풀 수 있다. 그랬을 때 시간복잡도는 아마 O(v^2)이다. 11403번 같이 간선에 비중이 없는 경우엔, 플로이드 와샬을 쓸 필요가 없다! 그냥 이럴 땐 bfs 탐색 쓰자.

  

- find-union : [6091_핑크플로이드](https://www.acmicpc.net/problem/6091)

  코드 자체는 간단하다. 속해있는 집합의 대표 원소를 찾는 find 함수와 두 원소가 속한 각각의 집합을 합치는 union 함수 2개를 만들면 끝. 처음에 할 땐 이것을 어디다 쓰나 싶었는데, 어제 푼 15586 무튜브 문제같이 원소와 원소간에 연결되어 있는지 확인할 때 bfs / dfs 보다 훨씬 편리한 것 같다.
  파이썬으로 하다보니 find 함수의 재귀 부분에서 오래 걸릴 때가 있다. find-union의 상위 호환 개념도 있을지도?

  

- 최소스패닝트리 : [6091_핑크플로이드](https://www.acmicpc.net/problem/6091)

  개념을 아직 찾아보진 않았다. 이렇게 하면 되지 않을까? 하고 푼 알고리즘이었는데 다행히 맞았다. 최소 길이의 간선을 차례대로 뽑아내고, 그 간선이 find-union으로 연결되지 않은 두 점을 잇고 있다면 그래프에 추가하는 식으로 진행했다. 트리 구조는 간선의 개수가 노드의 개수보다 1 작은 점을 이용했다. 시간 나면 제대로 정리한 글을 한 번은 읽어보는 게 좋을 것 같다. 

## 0208
- KMP : [1305_광고](https://www.acmicpc.net/problem/1305) [11585_속타는저녁메뉴](https://www.acmicpc.net/problem/11585)

  글자를 찾는 메커니즘까지는 이해하지 못했고, 일단은 가장 길면서 길이가 같은 preffix 와 suffix를 구하는 것 정도? check_fix로 작성하였고, 시간복잡도가 O(n) 밖에 안 된다. 1305 광고 문제에서 이전에 만들었던 함수는 O(n^2)이니 새로 짠 게 훨씬 빠르다. 어차피 KMP 전체 알고리즘을 다 쓸 시간에 Python find 함수를 쓰면 되니 이 정도만 알아도 될 듯.



## 0209

- 비트마스크 : [12920_평범한배낭2](https://www.acmicpc.net/problem/12920)

  모든 수는, 자신보다 작은 2의 제곱수의 합으로 표현 가능한 점을 이용했다. 제대로 비트마스크를 이해한 건지는 잘 모르겠다... 이 배낭 문제 같은 경우엔 10000개의 같은 물건을 하나씩 dp를 돌리는 게 아니라, 1,2,4,...,8192개의 물건을 한 번에 dp를 진행한다고 생각하면 되겠다. 즉, 10000번 dp돌릴것을 13번 만에 해결하는 것이다. 이전에 비트마스크를 처음 접했을 땐 뭐 어쩌라는 거지? 싶었는데 이렇게 문제에서 활용하고 나니 다 써먹을 데가 있다는 걸 느꼈다. 적용하기 많이 어렵지 않으니 다른 문제에서도 많이 활용해보자.



## 0210

- 다익스트라 : [1753_최단경로](https://www.acmicpc.net/problem/1753)

  사실 플루이드 와샬 보기 전에 이 놈을 먼저 봤어야 했다 ㅋㅋㅋ 근데 오히려 잘 이해가 안 됐다. 힙구조를 쓴 부분이 잘 이해가 가지 않는다. 해당 부분을 처음엔 덱으로 구현하였는데, 답은 맞은 거 같지만 메모리 초과가 떴다. 덱이 힙구조보다 메모리를 많이 잡아먹었을지도? 암튼 이해가 더 필요하다. 최솟값을 뽑아서 써야 하는 이유는 나중에 더 생각해보자.
  
- 다익스트라 : [1916_최소 비용 구하기](https://www.acmicpc.net/problem/1916)

  한 문제 더 풀어보니 조금 감이 잡히긴 한다. 힙구조를 사용해야 효율적인 탐색이 가능할 것이다. 그리고 힙구조에서 나온 경로값이 이미 낡은 데이터일 수가 있다. 그런 경우엔 탐색을 안 해주도록 하였다. 다른 최적화할만한 포인트가 있으려나?



## 0211

- 위상정렬: [1948 임계경로](https://www.acmicpc.net/problem/1948)

  처음에는 거리가 갱신되는 노드에 대해서 가능한 경로를 모두 들고 다니도록 하였는데, 메모리 초과가 떴다. 이후 어제 풀었던 다익스트라 문제가 생각나서 경로값이 낡은 경우 갱신을 하지 않도록 해주어 연산량을 줄여줬으나, 이젠 시간 초과가 떴다. 풀이 접근 방법이 잘못 된 것 같아 다시 생각해보니, 최대 경로가 하나 존재하고 각 노드 별 거리를 구했다면, 도착지에서 역으로 한 칸씩 이동하며 최대 경로를 찾을 수 있었다. 



## 0212

- Find-Union: 그냥 이 녀석은 무적이다. 쓸 구석이 너무 많다. 처음에 분리 집합을 접했을 땐, '이건 또 어따 쓰라는겨'라고 생각했는데, 사실상 백준 점수 올리는 데 이 녀석이 큰일을 했다. 파인드 유니온 영원하라~~
