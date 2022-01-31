# 7662 이중 우선순위 큐
# 출력값은 잘 나오는데 시간 초과 이슈
# bottleneck : remove함수 쓴 부분. 최적화 가능?
# 제거된 원소를 모아놓은 힙 생성? 그 힙 안에 있으면 넘어가기? 는 안 됨 같은 원소 여러개 있을 수 있다
# nlogn 정렬을 여러번 하기 총 n번 -> remove랑 다를게 없다
# 

import heapq
from sys import stdin as s


N = int(s.readline())
for _ in range(N):
	n = int(s.readline())
	min_heap = [ ]
	max_heap = [ ]
	cnt = 0
	for _ in range(n):
		order = s.readline().split()
		if order[0] == 'I':
			cnt += 1
			heapq.heappush(min_heap, int(order[1]))
			heapq.heappush(max_heap, -int(order[1]))
		elif cnt <= 1:
			cnt = 0
			min_heap = [ ]
			max_heap = [ ]
		else:
			cnt -= 1
			if order[1] == '-1':
				x = heapq.heappop(min_heap)
				max_heap.remove(-x)
			else:
				y = heapq.heappop(max_heap)
				min_heap.remove(-y)
	if cnt:
		print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
	else:
		print('EMPTY')