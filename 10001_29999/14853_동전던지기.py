from sys import stdin

input = stdin.readline

t = int(input())
query = [tuple(map(int, input().split())) for _ in range(t)]
ans = [0] * t
for tc in range(t):
    n1, m1, n2, m2 = query[tc]
    now = 1
    for k in range(m1 + 1):
        now *= n1 + 1 - k
        now /= n1 + n2 + 2 - k
    ans[tc] += now
    for k in range(1, m2 + 1):
        now *= ((m1 + k) * (n2 - k + 2)) / (k * (n1 + n2 - m1 - k + 2))
        ans[tc] += now
print(*ans, sep='\n')
