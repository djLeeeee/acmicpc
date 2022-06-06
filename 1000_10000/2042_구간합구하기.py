from sys import stdin
from collections import defaultdict

input = stdin.readline


def update(node, s, e):
    tree[node] += t
    if s == e:
        return
    mid = (s + e) // 2
    if mid < target:
        update(node * 2 + 1, mid + 1, e)
    else:
        update(node * 2, s, mid)


def get_sum(node, s, e, start, end):
    if s > e:
        return
    if start == s and end == e:
        return tree[node]
    mid = (s + e) // 2
    if mid < start:
        return get_sum(2 * node + 1, mid + 1, e, start, end)
    elif mid >= end:
        return get_sum(2 * node, s, mid, start, end)
    else:
        return get_sum(2 * node + 1, mid + 1, e, mid + 1, end) + get_sum(2 * node, s, mid, start, mid)


n, m, k = map(int, input().split())
tree = defaultdict(int)
arr = []
for target in range(n):
    t = int(input())
    arr.append(t)
    update(1, 0, n - 1)
for _ in range(m + k):
    state, init, fin = map(int, input().split())
    if state == 1:
        t = fin - arr[init - 1]
        target = init - 1
        arr[init - 1] = fin
        update(1, 0, n - 1)
    elif state == 2:
        print(get_sum(1, 0, n - 1, init - 1, fin - 1))
