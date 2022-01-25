from sys import stdin as s

def backpacking(N, M, mass, value):
    if N <= 0 or M < 0:
        return 0
    if mass[N] > M:
        return backpacking(N - 1, M, mass, value)
    x = backpacking(N - 1, M - mass[N], mass, value) + value[N]
    y = backpacking(N - 1, M, mass, value)
    return max(x, y)

N, M = map(int, s.readline().split())
mass = [ 0 ]
value = [ 0 ]
for _ in range(N):
    m, v = map(int, s.readline().split())
    mass.append(m)
    value.append(v)
print(backpacking(N, M, mass, value))