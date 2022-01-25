# 백준 2644
# https://www.acmicpc.net/problem/2644
# 32704KB, 88ms
from collections import deque

def bfs(x):
    S = deque([x])
    while S:
        p = S.popleft()
        for i in G[p]:
            if i == b:
                return visit[p]
            if not visit[i]:
                visit[i] = visit[p] + 1
                S.append(i)
    return -1
    
n = int(input())
a, b = map(int, input().split())
G = [[] for _ in range(n+1)]
for i in range(int(input())):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
visit = [0]*(n+1)
visit[a] = 1
print(bfs(a))