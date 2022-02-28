from sys import stdin as s
from sys import setrecursionlimit as st

st(10 ** 6)

input = s.readline

n = int(input())
in_order = input().split()
position = {}
for i in range(n):
    position[in_order[i]] = i
first_order = input().split()


def make_free(io_s, io_e, fo_s, fo_e):
    if io_s > io_e or fo_s > fo_e:
        return
    print(first_order[fo_e], end=' ')
    idx = position[first_order[fo_e]]
    make_free(io_s, idx - 1, fo_s, idx - io_s + fo_s - 1)
    make_free(idx + 1, io_e, fo_e - io_e + idx, fo_e - 1)


make_free(0, n - 1, 0, n - 1)
