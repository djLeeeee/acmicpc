from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tree = [0] * (2 * n + 1)
for _ in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, s, e, k = query
        left = s + n - 1
        right = e + n - 1
        while left <= right:
            if left % 2:
                tree[left] += k
                left += 1
            if not right % 2:
                tree[right] += k
                right -= 1
            left //= 2
            right //= 2
    elif query[0] == 2:
        _, x = query
        ans = arr[x - 1]
        ex = 0
        idx = x + n - 1
        while idx > 0:
            ex += tree[idx]
            idx //= 2
        print(ans + ex)
