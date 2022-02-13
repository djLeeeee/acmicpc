# 2637 장난감 조립
# 위상정렬 + 딕셔너리 활용 + 깊은 복사 대환장 콜라보
# 깊은복사 문제 해결하면 코드 길이 더 줄일 수 있을 듯.

from sys import stdin as s
from collections import deque

n = int(s.readline())
connection = [[ ] for _ in range(n + 1)]
get_in = [0] * (n + 1)

m = int(s.readline())
child = set()
for _ in range(m):
    x, y, k = map(int, s.readline().split())
    get_in[x] += 1
    connection[y].append([x, k])
    child.update([x])

parents = deque()
for i in range(1, n + 1):
    if get_in[i] == 0:
        parents.append(i)

xx = sorted(list(parents))

combined = { }
for k in child:
    necessary = { }
    for j in parents:
        necessary[j] = 0
    combined[k] = necessary

for p in parents:
    a = { }
    for j in parents:
        a[j] = 0
    combined[p] = a
    combined[p][p] = 1

while parents:
    now = parents.popleft()
    for i in connection[now]:
        get_in[i[0]] -= 1
        if get_in[i[0]] == 0:
            parents.append(i[0])
        for key in necessary.keys():
            combined[i[0]][key] += combined[now][key] * i[1]
 
for i in xx:
    print(f'{i} {combined[n][i]}')