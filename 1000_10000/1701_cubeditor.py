# 1701 Cube editor
# 2022-02-16 현재 문제 : 기존 pi 함수는 접두사 접미사만 체크
# 문제에선 중간에서 시작하는? 접두사도 체크해야함
# 예시) abbba 답 2 (bb) 현재 1 (a)

from sys import stdin as s


def max_fix(target):
    n = len(target)
    pi = [0] * n
    idx = 0
    for i in range(1, n):
        while idx > 0 and target[idx] != target[i]:
            idx = pi[idx - 1]
        if target[idx] == target[i]:
            idx += 1
            pi[i] = idx
    return max(pi)


editor = s.readline().strip()
length = len(editor)
ans = 0
for j in range(length - 1):
    ans = max(ans, max_fix(editor[j:]))
print(ans)
