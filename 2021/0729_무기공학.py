# 백준 18430 무기공학
# https://www.acmicpc.net/problem/18430
# 29200KB, 1340ms

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [(0,1), (-1,0), (-1,0), (0,1)]
dc = [(-1,0), (0,-1), (0,1), (1,0)]

visit = [[0]*m for _ in range(n)]

max_strength = 0

def dfs(idx, strength):
    global max_strength
    if idx == n*m:
        if strength > max_strength:
            max_strength = strength
        return
    r = idx // m
    c = idx % m
    dfs(idx+1, strength)
    if not visit[r][c]:
        for i in range(4):
            nr1 = r + dr[i][0]
            nc1 = c + dc[i][0]
            nr2 = r + dr[i][1]
            nc2 = c + dc[i][1]
            if nr1 < 0 or nr1 >= n or nc1 < 0 or nc1 >= m or nr2 < 0 or nr2 >= n or nc2 < 0 or nc2 >= m: continue
            if visit[nr1][nc1] or visit[nr2][nc2]: continue
            visit[r][c] = 1
            visit[nr1][nc1] = 1
            visit[nr2][nc2] = 1
            dfs(idx+1, strength + arr[r][c] * 2 + arr[nr1][nc1] + arr[nr2][nc2])
            visit[r][c] = 0
            visit[nr1][nc1] = 0
            visit[nr2][nc2] = 0

dfs(0,0)
print(max_strength)