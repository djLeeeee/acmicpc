import sys
sys.setrecursionlimit(10**4)

def insect(g, a, b):
    if 0 <= a < x and 0 <= b < y and g[b][a] == 1:
        g[b][a] = 0
        insect(g, a - 1, b)
        insect(g, a, b - 1)
        insect(g, a + 1, b)
        insect(g, a, b + 1)

t = int(sys.stdin.readline())
for _ in range(t):
    x, y, n = map(int, sys.stdin.readline().split())
    bachu = [[0] * x for _ in range(y)]
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        bachu[b][a] = 1
    result = 0
    for i in range(y):
        for j in range(x):
            if bachu[i][j]:
                insect(bachu, j, i)
                result += 1
    print(result)