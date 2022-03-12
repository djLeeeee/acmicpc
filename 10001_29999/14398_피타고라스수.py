from sys import stdin

input = stdin.readline


def check(a, b):
    x = a ** 2 + b ** 2
    if int(x ** 0.5) ** 2 == x:
        return True
    return False


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def dfs(x):
    for adj in graph[x]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = x
            return 1
    return 0


n = int(input())
nums = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    for j in range(i + 1, n):
        if check(nums[i], nums[j]) and gcd(nums[i], nums[j]) == 1:
            graph[i + 1].append(j + 1)
            graph[j + 1].append(i + 1)
match = [0] * (n + 1)
ans = 0
for k in range(1, n + 1):
    visited = [False] * (n + 1)
    ans += dfs(k)
print(ans // 2)
