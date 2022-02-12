# 2252 줄세우기
# 위상정렬 맛보기

########################################################
# 시간초과 코드(수정 완료)
# 뒤에서 역순으로 진행(뻗어나가는 간선이 없는 노드를 찾음)
# 매번 connection을 뒤져서 leaves를 갱신하는 것은 별로다.
# 자신에게서 나가는 간선의 수를 나타낸 get_out 사용
# get_out이 0인 노드는 leaf일 것이다!
# deque 기능을 적절히 잘 사용해야 한다... 덱 사용 더 연습해보자.

from sys import stdin as s
from collections import deque

n, m = map(int, s.readline().split())

connection = [ [ ] for _ in range(n + 1) ]
# 역방향
# get_out = [0] * (n + 1)

# for i in range(m):
#     x, y = map(int, s.readline().split())
#     connection[y].append(x)
#     get_out[x] += 1

# result = deque([])
# leaves = deque([])
# for i in range(1, n + 1):
#     if get_out[i] == 0:
#         leaves.append(i)
# while leaves:
#     a = leaves.popleft()
#     result.appendleft(a)
#     for j in connection[a]:
#         get_out[j] -= 1
#         if get_out[j] == 0:
#             leaves.append(j)
# print(*result)

# 정방향
get_in = [0] * (n + 1)

for i in range(m):
    x, y = map(int, s.readline().split())
    connection[x].append(y)
    get_in[y] += 1

parents = deque([])
for i in range(1, n + 1):
    if get_in[i] == 0:
        parents.append(i)
while parents:
    a = parents.popleft()
    print(a, end = ' ')
    for j in connection[a]:
        get_in[j] -= 1
        if get_in[j] == 0:
            parents.append(j)