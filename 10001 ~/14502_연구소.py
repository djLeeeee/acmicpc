# 2차원 리스트 딥카피 안 쓰고 그냥 함수값으로 주면 안 됨
# 깊은 복사 얕은 복사 신경 쓰자

from sys import stdin as s
import copy

m, n = map(int, s.readline().split())
empty = [ ]
virus = [ ]
labatory = [ ]
for i in range(m):
    line = list(map(int, s.readline().split()))
    for j in range(n):
        if line[j] == 0:
            empty.append([i, j])
        elif line[j] == 2:
            virus.append([i, j])
    labatory.append(line)

def safety(w1, w2, w3):
    lab = copy.deepcopy(labatory)
    lab[w1[0]][w1[1]] = 1
    lab[w2[0]][w2[1]] = 1
    lab[w3[0]][w3[1]] = 1
    lx = len(lab)
    ly = len(lab[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    start = copy.deepcopy(virus)
    while start:
        new_start = [ ]
        for st in start:
            x = st[0]
            y = st[1]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < lx and 0 <= ny < ly and lab[nx][ny] == 0:
                    lab[nx][ny] = 2
                    new_start.append([nx, ny])
        start = new_start[:]
    result = 0
    for i in lab:
        for j in i:
            if j == 0:
                result += 1
    return result

ans = 0
l = len(empty)
for x in range(2, l):
    for y in range(1, x):
        for z in range(y):
            ans = max(ans, safety(empty[z], empty[y], empty[x]))
print(ans)