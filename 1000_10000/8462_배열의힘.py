from sys import stdin

input = stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for idx in range(t):
    s, e = map(int, input().split())
    queries.append((s - 1, e - 1, idx))
sn = n ** 0.5
queries.sort(key=lambda z: (z[0] // sn, z[1]))
ans = [0] * t
ps, pe, idx = queries[0]
cnt = {}
for i in range(ps, pe + 1):
    if arr[i] not in cnt:
        cnt[arr[i]] = 1
    else:
        cnt[arr[i]] += 1
for x, y in cnt.items():
    ans[idx] += y * y * x
pa = ans[idx]
for s, e, idx in queries[1:]:
    if s < ps:
        for i in range(s, ps):
            if arr[i] not in cnt:
                cnt[arr[i]] = 1
            else:
                cnt[arr[i]] += 1
            pa += arr[i] * (2 * cnt[arr[i]] - 1)
    elif s > ps:
        for i in range(ps, s):
            if arr[i] not in cnt:
                cnt[arr[i]] = -1
            else:
                cnt[arr[i]] -= 1
            pa -= arr[i] * (2 * cnt[arr[i]] + 1)
    if e > pe:
        for i in range(pe + 1, e + 1):
            if arr[i] not in cnt:
                cnt[arr[i]] = 1
            else:
                cnt[arr[i]] += 1
            pa += arr[i] * (2 * cnt[arr[i]] - 1)
    elif e < pe:
        for i in range(e + 1, pe + 1):
            if arr[i] not in cnt:
                cnt[arr[i]] = -1
            else:
                cnt[arr[i]] -= 1
            pa -= arr[i] * (2 * cnt[arr[i]] + 1)
    ans[idx] = pa
    ps, pe = s, e
print(*ans, sep='\n')
