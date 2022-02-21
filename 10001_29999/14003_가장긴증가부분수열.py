# 14003 가장 긴 증가하는 부분 수열5
# 이분 탐색

from sys import stdin as s

input = s.readline


def search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if array[middle] < target:
            start = middle + 1
        else:
            result = middle
            end = middle - 1
    return result


n = int(input())
nums = list(map(int, input().split()))
stack = [nums[0]]
a = [0] * n
a[0] = 1
length = 1
for i in range(1, n):
    if stack[-1] < nums[i]:
        stack.append(nums[i])
        length += 1
        a[i] = length
    else:
        idx = search(stack, nums[i])
        a[i] = idx + 1
        stack[idx] = nums[i]
print(length)
ans = [0] * length
j = n - 1
while length > 0:
    if a[j] == length:
        length -= 1
        ans[length] = nums[j]
    j -= 1
print(*ans)
