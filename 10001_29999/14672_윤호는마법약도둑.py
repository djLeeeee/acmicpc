from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 4)


def make_p_set():
    check = [1] * 10001
    result = set()
    for i in range(2, 10001):
        if check[i]:
            result.add(i)
            for j in range(2 * i, 10001, i):
                check[j] = 0
    return result


def div(k):
    if k in prime_set:
        return [k]
    result = []
    for p in prime_set:
        if k % p == 0:
            while k % p == 0:
                k //= p
            result.append(p)
            if k == 1:
                return result
    return result + [k]


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


_, m = map(int, input().split())
prime_set = make_p_set()
graph = [0] + [div(i) for i in map(int, input().split())]
match = defaultdict(int)
ans = 0
for i in range(1, m + 1):
    visited = defaultdict(bool)
    ans += dfs(i)
print(ans)
