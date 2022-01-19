import sys

# Input : graph / initial point / # of points 
# Output : # of recommendation videos
def recommendation(G,a,n,lim):
    result = [ lim ] * (n+1)
    visited = [a]
    new_visited = [a]
    while True:
        for i in range( len(new_visited) ):
            x = []
            for key,value in G.items():
                if new_visited[i] in key:
                    new_point = key[1] if key[0] == new_visited[i] else key[0]
                    if new_point not in visited:
                        result[new_point] = min( value, result[new_visited[i]] )
                        x.append(new_point)
        new_visited = x
        if len(new_visited) == 0:
            break
        visited += new_visited
    return result.count(lim)-2

N,T = map(int,sys.stdin.readline().split())

# Graph를 Dictionary로 표현
graph={}
for _ in range(N-1):
    x,y,rel = map(int, sys.stdin.readline().split())
    if x == y:
        continue
    graph[ (x,y) ] = rel

# 정답 출력
for _ in range(T):
    K,init = map(int, sys.stdin.readline().split())
    print(recommendation(graph, init, N, K))