from sys import stdin
from collections import defaultdict

input = stdin.readline


def sol():
    ans = sum(team1) + sum(team2)
    for bs in range(n // 2 + 1):
        l, r = point(bs), point(n // 2 - bs, True)
        ll, lr = len(l), len(r)
        l_key, r_key = sorted(l), sorted(r, reverse=True)
        pointer1, pointer2 = 0, 0
        while pointer1 < ll and pointer2 < lr:
            now = l_key[pointer1] + r_key[pointer2]
            if ans > abs(now):
                ans = abs(now)
                team = l[l_key[pointer1]] + r[r_key[pointer2]]
            elif ans == abs(now):
                team = min(team, l[l_key[pointer1]] + r[r_key[pointer2]])
            if now > 0:
                pointer2 += 1
            elif now < 0:
                pointer1 += 1
            else:
                pointer1 += 1
                pointer2 += 1
    return team


def point(bs, right=False):
    result = {}
    ex = n // 2 if right else 0
    for bit in cnt[bs]:
        a = 0
        for b in range(n // 2):
            if bit & 1 << b:
                a += team2[b + ex]
            else:
                a -= team1[b + ex]
        if a in result:
            result[a] = min(result[a], trans(bit))
        else:
            result[a] = trans(bit)
    return result


def trans(x):
    result = []
    for bit in range(n // 2):
        if x & 1 << bit:
            result.append(2)
        else:
            result.append(1)
    return result


n = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))
cnt = defaultdict(list)
for i in range(1 << (n // 2)):
    cnt[sum(map(int, bin(i)[2:]))].append(i)
print(*sol())
