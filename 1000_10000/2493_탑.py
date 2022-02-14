# 2493 탑

from sys import stdin as s

n = int(s.readline())
array = list(map(int, s.readline().split()))
ans = [0] * n
remain = [n - 1]
for i in range(1, n):
    while remain and array[remain[-1]] <= array[n - i - 1]:
        ans[remain.pop()] = n - i
    remain.append(n - i - 1)
print(*ans)
