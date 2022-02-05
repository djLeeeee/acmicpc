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
