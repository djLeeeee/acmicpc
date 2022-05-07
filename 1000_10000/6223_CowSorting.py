from sys import stdin

input = stdin.readline


def sol(idx):
    if nums[idx] == result[idx]:
        return 0
    cycle = set()
    while nums[idx] not in cycle:
        cycle.add(nums[idx])
        idx = inv[nums[idx]]
    for num in cycle:
        nums[inv[num]] = num
    m = min(cycle)
    l = len(cycle)
    return sum(cycle) + min(m + result[0] * (l + 1), (l - 2) * m)


n = int(input())
nums = [int(input()) for _ in range(n)]
result = sorted(nums)
inv = {result[i]: i for i in range(n)}
ans = 0
for j in range(n):
    ans += sol(j)
print(ans)
