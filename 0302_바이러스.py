def dfs(v):
    visit[v] = 1
    for w in G[v]:
        if visit[w] == 0:
            dfs(w)
    return sum(visit) - 1 # 1번 컴퓨터 빼고 세야 함

n = int(input())
m = int(input())
G = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
visit = [0] * (n+1)
print(dfs(1))
