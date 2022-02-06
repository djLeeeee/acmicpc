# 7662 이중 우선순위 큐
# 출력값은 잘 나오는데 시간 초과 이슈
# bottleneck : remove함수 쓴 부분. 최적화 가능?
# 제거된 원소를 모아놓은 힙 생성? 그 힙 안에 있으면 넘어가기? 는 안 됨 같은 원소 여러개 있을 수 있다
# nlogn 정렬을 여러번 하기 총 n번 -> remove랑 다를게 없다
# 2022/02/06 방문 여부를 체크하는 done 변수 추가
# 마참내!

import heapq
from sys import stdin as s

N = int(s.readline())
for _ in range(N):
	n = int(s.readline())
	min_heap = [ ]
	max_heap = [ ]
	cnt = 0
	done = [False] * 1000001
	for i in range(n):
		order = s.readline().split()
		if order[0] == 'I':
			cnt += 1
			heapq.heappush(min_heap, (int(order[1]), i))
			heapq.heappush(max_heap, (-int(order[1]), i))
		elif cnt == 0:
			min_heap = [ ]
			max_heap = [ ]
		else:
			cnt -= 1
			if order[1] == '-1':
				while min_heap:
					x = heapq.heappop(min_heap)
					if not done[x[1]]:
						done[x[1]] = True
						break								
			else:
				while max_heap:
					y = heapq.heappop(max_heap)
					if not done[y[1]]:
						done[y[1]] = True
						break				
	# 마지막 갱신. 아래 4줄이 제일 중요함!
	while min_heap and done[min_heap[0][1]]:
		heapq.heappop(min_heap)
	while max_heap and done[max_heap[0][1]]:
		heapq.heappop(max_heap)
	
	if cnt:
		print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
	else:
		print('EMPTY')