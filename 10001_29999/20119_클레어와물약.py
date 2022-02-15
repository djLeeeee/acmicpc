# 20119 클레어와 물약
# 이걸 어떻게 그래프로 표현 ????
# 그래프 (필요한 거) -> (완성품)으로 하고,
# 가지고 있는 물품에 대해선 들어오는 간선 모두 제거
# 이후 똑같이 위상 정렬
# 20220215 2트 / 현재 문제점 : 한 물약에 대해서 레시피가 여러 개 있는 경우
# 해결방안 : connection 의 요소를 dictionary 로 받기?
# 구현은 가능할 듯. 근데 탐색 시간 엄청 걸릴 듯? 종료 조건은 딕셔너리가 빌 때까지?
# 다른 방법....
# 결국 통과! receipt 을 넘버링해 재료를 다 모은 receipt 을 확인해줬다

from sys import stdin as s
from collections import deque

n, m = map(int, s.readline().split())
connection = [[] for _ in range(n + 1)]
receipt_need = [0] * m
for j in range(m):
    new_receipt = list(map(int, s.readline().split()))
    for i in new_receipt[1:-1]:
        connection[i].append((j, new_receipt[-1]))
    receipt_need[j] = new_receipt[0]
L = int(s.readline())
can_make = deque(map(int, s.readline().split()))
ans = set()
while can_make:
    now = can_make.popleft()
    if now in ans:
        continue
    ans.add(now)
    for idx, target in connection[now]:
        receipt_need[idx] -= 1
        if receipt_need[idx] == 0:
            can_make.append(target)
print(len(ans))
print(*sorted(list(ans)))
