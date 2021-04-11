# 백준 2583
import sys
sys.setrecursionlimit(10**6)

def dfs(r,c):
    global cnt
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr > -1 and nr < n and nc > -1 and nc < m:
            if not arr[nr][nc]:
                arr[nr][nc] = 1
                cnt += 1
                dfs(nr,nc)
                
n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1,r2):
        for j in range(c1,c2):
            arr[i][j] = 1

dr = [0,1,0,-1]
dc = [1,0,-1,0]
ls = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            arr[i][j] = 1
            cnt = 1
            dfs(i,j)
            ls.append(cnt)
print(len(ls))
print(*sorted(ls))