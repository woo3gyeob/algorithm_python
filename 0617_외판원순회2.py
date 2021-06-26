def dfs(node, cost, cnt):
    global min_cost
    if cost >= min_cost: #가지치기용
        return
    if cnt == n:
        if not W[node][start]: return
        cost += W[node][start]
        if cost >= min_cost:
            return
        min_cost = cost
        return
    for i in range(n):
        if visit[i] or not W[node][i]: continue
        visit[i] = 1
        dfs(i, cost+W[node][i], cnt+1)
        visit[i] = 0

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
visit = [0]*n
min_cost = 0xfffffff
for start in range(n):
    visit[start] = 1
    dfs(start, 0, 1)
    visit[start] = 0

print(min_cost)