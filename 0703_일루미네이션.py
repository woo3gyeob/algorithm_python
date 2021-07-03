import sys
sys.setrecursionlimit(10**7)
from collections import deque

dr = [-1,0,1,1,0,-1]
doc = [0,-1,0,1,1,1]
dec = [-1,-1,-1,0,1,0]

m, n = map(int, input().split())
arr = []
arr.append([0]*(m+2))
for _ in range(n):
    ls = [0] + list(map(int, input().split())) + [0]
    arr.append(ls)
arr.append([0]*(m+2))

S = deque([(0,0)])

while S:
    r, c = S.popleft()
    for i in range(6):
        nr = r + dr[i]
        if r % 2:
            nc = c + doc[i]
        else:
            nc = c + dec[i]
        if nr >= n+2 or nr < 0 or nc >= m+2 or nc < 0: continue
        if arr[nr][nc] == 0:
            arr[nr][nc] = -1
            S.append((nr,nc))

wall_len = 0

visit = [[0]*(m+2) for _ in range(n+2)]

def dfs(r, c):
    global wall_len
    for i in range(6):
        nr = r + dr[i]
        if r % 2 == 1:
            nc = c + doc[i]
        else:
            nc = c + dec[i]
        if arr[nr][nc] == 1 and not visit[nr][nc]:
            visit[nr][nc] = 1
            dfs(nr,nc)
        if arr[nr][nc] == -1:
            wall_len += 1

for i in range(n+1):
    for j in range(1, m+1):
        if arr[i][j] == 1 and not visit[i][j]:
            visit[i][j] = 1
            dfs(i,j)

print(wall_len)