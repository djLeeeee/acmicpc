# 1786 찾기
# KMP 알고리즘 / 더 연습 필요

t = input()
n = len(t)
p = input()
m = len(p)
pi = [0] * m
idx = 0
for i in range(1, m):
    while idx > 0 and p[i] != p[idx]:
        idx = pi[idx - 1]
    if p[i] == p[idx]:
        idx += 1
        pi[i] = idx
result = []
ans = 0
j = 0
for k in range(n):
    while j > 0 and t[k] != p[j]:
        j = pi[j - 1]
    if t[k] == p[j]:
        if j == m - 1:
            ans += 1
            result.append(k + 2 - m)
            j = pi[j]
        else:
            j += 1
print(ans)
print(*result)
