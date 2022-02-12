from sys import stdin as s

def BFS(line, start): # 너비 우선 (2)
    result = [start]
    start_points = result
    n = 0
    ans = 0
    while start_points:
        new_visit = []
        for i in start_points:
            for j in line[i]:
                if j not in result and j not in new_visit:
                    new_visit.append(j)
        result += new_visit
        start_points = new_visit
        n += 1
        ans += n * len(start_points)
    return ans

N, M = map( int, s.readline().split() ) # 변수 받기

line = [ set() for i in range(N + 1) ] # line graph 생성 (2)
for _ in range(M):
    x, y = map( int, s.readline().split() )
    line[x].update([y])
    line[y].update([x])

min_kn = BFS(line, 1)
ans = 1
for i in range(2, N + 1):
    kn = BFS(line, i)
    if min_kn > kn:
        min_kn = kn
        ans = i
print(ans)