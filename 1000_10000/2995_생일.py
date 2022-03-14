from sys import stdin

input = stdin.readline


def find(start, end, target):
    while start <= end:
        middle = (start + end) // 2
        if stack[middle] < target:
            res = middle
            end = middle - 1
        else:
            start = middle + 1
    return res


n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]
nums.sort(key=lambda xx: xx[1], reverse=True)
nums.sort(key=lambda xx: xx[0])
dp = [0] * n
dp[0] = 1
ans = 1
stack = [nums[0][1]]
for i in range(1, n):
    if stack[-1] >= nums[i][1]:
        stack.append(nums[i][1])
        ans += 1
        dp[i] = ans
    else:
        idx = find(0, ans - 1, nums[i][1])
        stack[idx] = nums[i][1]
        dp[i] = idx + 1
print(ans)
query = [[] for _ in range(ans)]
check = n - 1
while ans > 0:
    if dp[check] == ans:
        ans -= 1
        query[ans] = nums[check]
    check -= 1
for line in query:
    print(*line)
