from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
querys = []
m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    querys.append((s - 1, e - 1, i))
sn = n ** 0.5
querys.sort(key=lambda x: (x[0] // sn, x[1]))
ans = [0] * m
cnt = defaultdict(int)
cnt_inv = defaultdict(int)
cnt_inv[0] = n
ps, pe, _ = querys[0]
for idx in range(ps, pe + 1):
    cnt_inv[cnt[arr[idx]]] -= 1
    cnt[arr[idx]] += 1
    cnt_inv[cnt[arr[idx]]] += 1
mx = max(cnt.values())
for s, e, i in querys:
    if ps < s:
        for idx in range(ps, s):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    elif s < ps:
        for idx in range(s, ps):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx + 1]:
                mx += 1
    if pe < e:
        for idx in range(pe + 1, e + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] += 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx + 1]:
                mx += 1
    elif e < pe:
        for idx in range(e + 1, pe + 1):
            cnt_inv[cnt[arr[idx]]] -= 1
            cnt[arr[idx]] -= 1
            cnt_inv[cnt[arr[idx]]] += 1
            if not cnt_inv[mx]:
                mx -= 1
    ps, pe = s, e
    ans[i] = mx
print(*ans, sep='\n')
