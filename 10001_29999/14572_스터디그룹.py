from sys import stdin

input = stdin.readline

n, k, d = map(int, input().split())
algo = []
student = []
for i in range(n):
    _, c = map(int, input().split())
    algo.append(set(map(int, input().split())))
    student.append((c, i))
student.sort()
start = 0
end = 0
ans = 0
known = [0] * (k + 1)
tk, wk = 0, 0
while end < n:
    if student[end][0] - student[start][0] > d:
        for a in algo[student[start][1]]:
            known[a] -= 1
            if known[a] == 0:
                tk -= 1
        start += 1
    else:
        for a in algo[student[end][1]]:
            known[a] += 1
            if known[a] == 1:
                tk += 1
        wk = known.count(end - start + 1)
        ans = max(ans, (end - start + 1) * (tk - wk))
        end += 1
print(ans)
