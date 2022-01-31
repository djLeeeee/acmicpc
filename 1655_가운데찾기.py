# 1655 가운데를 말해요~
# 이분 탐색으로 원소 삽입?
# 힙 구조로는 가운데 원소 못 뽑음 아마도
# 가운데 값을 뽑기 위해서
# 힙 두개?
# 총 2n + 1개 일때 힙1 n 힙2 n+1 / 힙1 n 힙2 n... 힙2를 더 큰 쪽, 출력은 항상 힙2[0]
# 힙1은 min heap 힙2는 max heap 힙1에는 큰 n개 힙2에는 작은 n(+1)개
# 힙1의 모든 원소가 힙2보다 커야한다 -> 힙2[0] <= 힙1[0]
# 원소가 1개씩만 추가되기 때문에 위치를 바꿔줘야 하는 건 항상 많아야 두 개 밖에 없다

import heapq
from sys import stdin as s

n = int(s.readline())
min_heap = [ ]
max_heap = [ ]

for _ in range(n):
	a = int(s.readline())
	if len(min_heap) < len(max_heap):
		heapq.heappush(min_heap, a)
	else:
		heapq.heappush(max_heap, -a)

	if min_heap and max_heap[0] + min_heap[0] < 0:
		x = heapq.heappop(max_heap)
		y = heapq.heappop(min_heap)
		heapq.heappush(max_heap, -y)
		heapq.heappush(min_heap, -x)
	print(-max_heap[0])