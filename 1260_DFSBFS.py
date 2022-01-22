from sys import stdin as s

def DFS(line, start): # 깊이 우선 depth?
    result = [ ]
    need_visit = [start]
    while need_visit:
        x= need_visit.pop()
        if x not in result:
            result.append(x)
            for i in range(len(line) - 1, 0, -1):
                if line[x][i] == 1:
                    need_visit.append(i)
    return result

def BFS(line, start): # 너비 우선
    result = [start]
    start_points = result
    while True:
        new_visit = []
        for i in start_points:
            for j in range(len(line[i])):
                if line[i][j] == 1 and j not in result and j not in new_visit:
                    new_visit.append(j)
        result += new_visit
        start_point = new_visit
        if new_visit == []:
            break
    return result

N, M, V = map( int, s.readline().split() )

line = [ [0] * (N + 1) for _ in range(N + 1) ]

for _ in range(M):
    x, y = map( int, s.readline().split() )
    line[x][y] = 1
    line[y][x] = 1

print(*DFS(line, V))
print(*BFS(line, V))