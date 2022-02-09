# 10265 MT
# FIND-UNION 후 각 트리의 크기만큼으로 배낭문제 해결하면 될 듯?

# FIND-UNION 하고 나서 각 요소의 크기를 어떻게 받음??
# 파인드 유니온 다 돌리기 -> 각 원소들 다시 한 번 돌면서 {FIND() : 집합 원소 갯수} 의 딕셔너리 생성
# -> 딕셔너리의 VALUE 값으로 배낭 문제
# 딱히 연산량이 많지는 않을 듯?

from sys import stdin as s
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

n, k = map(int, s.readline().split())
parent = list(range(n + 1))

# find-union 방법 자체는 잘 구현했으나 틀린 방법임.
# 4번이 가야만 3번이 갈 수 있는 상황이지, 쌍방향이 아니다.
# 현재 풀이는 쌍방향인 경우.
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return


connection = list(map(int, s.readline().split()))
for idx, person in enumerate(connection):
    if idx + 1 != person:
        union(idx + 1, person)
group = {}
for i in range(1, n + 1):
    group[find(i)] = group.get(find(i), 0) + 1
dp = [0] * (k + 1)
for num in group.values():
    for now in range(k, num - 1, -1):
        dp[now] = max(dp[now], dp[now - num] + num)
print(dp[-1])
