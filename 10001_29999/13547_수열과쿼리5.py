from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
querys = []
q = int(input())
for i in range(q):
    s, e = map(int, input().split())
    querys.append((s - 1, e - 1, i))
sq = n ** 0.5
querys.sort(key=lambda x: (x[1] // sq, x[0], x[2]))
ans = [0] * q
check = defaultdict(int)
used = 0
s, e, idx = querys[0]
for i in range(s, e + 1):
    check[arr[i]] += 1
    if check[arr[i]] == 1:
        used += 1
ps, pe = s, e
ans[idx] = used
for s, e, idx in querys[1:]:
    if pe < s:
        check = defaultdict(int)
        used = 0
        for i in range(s, e + 1):
            check[arr[i]] += 1
            if check[arr[i]] == 1:
                used += 1
    else:
        if s > ps:
            for i in range(ps, s):
                check[arr[i]] -= 1
                if check[arr[i]] == 0:
                    used -= 1
        else:
            for i in range(s, ps):
                check[arr[i]] += 1
                if check[arr[i]] == 1:
                    used += 1
        if e > pe:
            for i in range(pe + 1, e + 1):
                check[arr[i]] += 1
                if check[arr[i]] == 1:
                    used += 1
        else:
            for i in range(e + 1, pe + 1):
                check[arr[i]] -= 1
                if check[arr[i]] == 0:
                    used -= 1
    ps, pe = s, e
    ans[idx] = used
print(*ans, sep='\n')
