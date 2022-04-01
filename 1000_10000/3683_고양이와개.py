from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


for _ in range(int(input())):
    c, d, v = map(int, input().split())
    cat_love = [[] for _ in range(c + 1)]
    cat_hate = [[] for _ in range(c + 1)]
    dog_love = [[] for _ in range(d + 1)]
    dog_hate = [[] for _ in range(d + 1)]
    cn = 0
    dn = 0
    for i in range(1, v + 1):
        like, hate = input().split()
        l_idx = int(like[1:])
        h_idx = int(hate[1:])
        if like[0] == 'C':
            cn += 1
            cat_love[l_idx].append(cn)
            dog_hate[h_idx].append(cn)
        else:
            dn += 1
            dog_love[l_idx].append(dn)
            cat_hate[h_idx].append(dn)
    graph = [[] for _ in range(cn + 1)]
    for i in range(1, c + 1):
        for li in cat_love[i]:
            for hi in cat_hate[i]:
                graph[li].append(hi)
    for i in range(1, d + 1):
        for hi in dog_hate[i]:
            for li in dog_love[i]:
                graph[hi].append(li)
    ans = v
    match = [0] * (dn + 1)
    for i in range(1, cn + 1):
        visited = [False] * (dn + 1)
        ans -= dfs(i)
    print(ans)
