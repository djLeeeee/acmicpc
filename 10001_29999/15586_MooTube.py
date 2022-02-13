# 15586 무튜브 추천영상 개수 구하기
# 오프라인 쿼리 개념 사용 -> 기억 안 나면 찾아보자. 별거 아님
# find-union을 여기서 쓰게 될 줄은 몰랐다.
# limit와 usado 정렬을 어떻게 할 지 정해주는 게 주요 포인트

# import sys

# # Input : graph / initial point / # of points 
# # Output : # of recommendation videos
# def recommendation(G,a,n,lim):
#     result = [ lim ] * (n+1)
#     visited = [a]
#     new_visited = [a]
#     while True:
#         for i in range( len(new_visited) ):
#             x = []
#             for key,value in G.items():
#                 if new_visited[i] in key:
#                     new_point = key[1] if key[0] == new_visited[i] else key[0]
#                     if new_point not in visited:
#                         result[new_point] = min( value, result[new_visited[i]] )
#                         x.append(new_point)
#         new_visited = x
#         if len(new_visited) == 0:
#             break
#         visited += new_visited
#     return result.count(lim)-2

# N,T = map(int,sys.stdin.readline().split())

# # Graph를 Dictionary로 표현
# graph={}
# for _ in range(N-1):
#     x,y,rel = map(int, sys.stdin.readline().split())
#     if x == y:
#         continue
#     graph[ (x,y) ] = rel

# # 정답 출력
# for _ in range(T):
#     K,init = map(int, sys.stdin.readline().split())
#     print(recommendation(graph, init, N, K))


# 15586 MooTube
# 2022/02/06 재도전
# 오프라인 쿼리 개념 사용해볼것

from sys import stdin as s

m, n = map(int, s.readline().split())
usado = [ ]
for i in range(m - 1):
    p, q, r = map(int, s.readline().split())
    usado.append((r, p, q))
usado.sort(reverse = True)
limit = [ ]
origin = [ ]
for j in range(n):
    k, v = map(int, s.readline().split())
    limit.append((k, j))
    origin.append(v)
limit.sort()

# 리미트 값이 높은 순으로 답을 구하는게 맞는 듯???
# find - union 개념 필요한 듯
parent = list(range(m + 1))
parent_num = [1] * (m + 1)
def find(target):
	if target == parent[target]:
		return target
	parent[target] = find(parent[target])
	return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = [0] * n
i = 0
while limit:
    a = limit.pop()
    limit_now = a[0]
    limit_index = a[1]
    # limit 값보다 작은 놈들을 find_union?
    # 그럼 limit 작은 놈을 먼저 하는게 맞지 않나?
    # limit 보다 작은 connection 처리해주고, find 값이 다르면 성공?
    while i <= m - 2 and usado[i][0] >= limit_now:
        x = usado[i][1]
        y = usado[i][2]
        a = parent_num[find(x)] + parent_num[find(y)]
        union(x, y)
        parent_num[find(x)] = a
        i += 1
    result[limit_index] = parent_num[find(origin[limit_index])] - 1
print(*result, sep = '\n')