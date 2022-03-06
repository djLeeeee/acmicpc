# 2568 전깃줄2
# DP + 이분 탐색 + 경로 역추적인듯??

from sys import stdin as s

input = s.readline


def div_find(array, target):
    start = 0
    end = len(array) - 1
    ans = end
    while start <= end:
        middle = (start + end) // 2
        if array[middle][1] < target[1]:
            start = middle + 1
        else:
            ans = middle
            end = middle - 1
    return ans


n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
dp = [0] * n
dp[0] = 1
stack = [lines[0]]
length = 1
for i in range(1, n):
    line = lines[i]
    if stack[-1][1] < line[1]:
        stack.append(line)
        length += 1
        dp[i] = length
    else:
        idx = div_find(stack, line)
        stack[idx] = line
        dp[i] = idx + 1
print(n - length)
pointer = -1
remain = set()
while length > 0:
    if dp[pointer] == length:
        remain.add(lines[pointer][0])
        length -= 1
    pointer -= 1
for j, _ in lines:
    if j not in remain:
        print(j)
