# 백준 온라인 문제풀이

## 1. 시간복잡도
https://wiki.python.org/moin/TimeComplexity

1. list :  LIFO 에 좋음
   - O(1) : `append` `pop` `len` my_list[1] = 3 (set data) ....
   - O(n): `popleft` `delete` `in` `insert` 
   - O(nlogn) : `sort` => 웬만한 sort는 다 이걸로 사용하자
2. set
   - O(1) : `in` 
   - O(n) : `update`(추가하려는 list의 길이에 비례) 

큐, 덱, 딕셔너리...