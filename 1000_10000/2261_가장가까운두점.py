# 2261 가장 가까운 두 점
# 3월 9일 TIL 참고
# 기하와 친해지기 프로젝트 1번
from sys import stdin

input = stdin.readline


def dist(p1: tuple, p2: tuple) -> int:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def divide(start, end):
    if start == end:
        return 100000
    if end - start == 1:
        return dist(point[start], point[end])
    middle = (start + end) // 2
    md = min(divide(start, middle), divide(middle, end))
    candidate = []
    for i in range(start, end + 1):
        if (point[middle][0] - point[i][0]) ** 2 < md:
            candidate.append(point[i])
    c = len(candidate)
    candidate.sort(key=lambda nn: nn[1])
    for j in range(c - 1):
        for k in range(j + 1, c):
            if (candidate[j][1] - candidate[k][1]) ** 2 < md:
                md = min(md, dist(candidate[j], candidate[k]))
            else:
                break
    return md


n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
point.sort()
print(divide(0, n - 1))
