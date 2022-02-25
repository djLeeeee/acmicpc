# 11780 플로이드2

from sys import stdin as s
from copy import deepcopy

input = s.readline

n = int(input())
m = int(input())
connection = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y, c = map(int, input().split())
    if connection[x][y]:
        connection[x][y] = min(connection[x][y], c)
    else:
        connection[x][y] = c
bus = deepcopy(connection)
for j in range(1, n + 1):
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            if i != k and connection[i][j] and connection[j][k]:
                if connection[i][k]:
                    connection[i][k] = min(
                        connection[i][k],
                        connection[i][j] + connection[j][k]
                    )
                else:
                    connection[i][k] = connection[i][j] + connection[j][k]
for line in connection[1:]:
    print(*line[1:])


def trace(start, end):
    if connection[start][end] == bus[start][end]:
        return []
    for idx in range(1, n + 1):
        if bus[start][idx] and bus[start][idx] + connection[idx][end] == connection[start][end]:
            return [idx] + trace(idx, end)


for p in range(1, n + 1):
    for q in range(1, n + 1):
        if connection[p][q]:
            x = trace(p, q)
            print(len(x) + 2, p, *x, q)
        else:
            print(0)
