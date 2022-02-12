# 20119 클레어와 물약
# 이걸 어떻게 그래프로 표현 ????
# 그래프 (필요한 거) -> (완성품)으로 하고,
# 가지고 있는 물품에 대해선 들어오는 간선 모두 제거
# 이후 똑같이 위상 정렬

from sys import stdin as s
from collections import deque

n, m = map(int, s.readline().split())
get_in = [0] * (n + 1)
connection = [[] for _ in range(n + 1)]
for _ in range(m):
    receipt = list(map(int, s.readline().split()))
    for i in receipt[1:-1]:
        connection[i].append(receipt[-1])
    get_in[receipt[-1]] += receipt[0]
k = int(s.readline())
ans = set(map(int, s.readline().split()))
init = deque(ans)
while init:
    now = init.popleft()
    for j in connection[now]:
        if j not in ans:
            get_in[j] -= 1
            if get_in[j] == 0:
                init.append(j)
                ans.add(j)
print(len(ans))
print(*sorted(list(ans)))
