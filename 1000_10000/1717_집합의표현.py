# 1717 집합의 표현
# find-union 방법
# parent = [1,2,3] => union(1,3) => parent = [1,2,1] => find(1) = 1, find(3) = 1, find(2) = 2
# 부모 아래 자식 요소가 많이 있는 K1,n 그래프 형태 생각하면 될 듯

from sys import stdin as s

def find(target):
	if target == parent[target]:
		return target
	parent[target] = find(parent[target]) # 이 부분이 필요한 이유: 재귀 횟수 줄일 수 있음
	return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 

n, m = map(int, s.readline().split())
parent = list(range(n + 1))
for _ in range(m):
	order, a, b = map(int, s.readline().split())
	if order:
		if find(a) == find(b):
			print('YES')
		else:
			print('NO')
	else:
		union(a, b)