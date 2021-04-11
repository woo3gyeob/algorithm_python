# 2589 보물섬
# pypy3 pass, python3 tle
def bfs(sr,sc):
    global distance
    S = [(sr,sc)]
    while S:
        distance += 1
        for _ in range(len(S)):
            point = S.pop(0)
            r, c = point[0], point[1]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr > -1 and nr < n and nc > -1 and nc < m:
                    if arr[nr][nc] == 'L' and D[nr][nc] == 0:
                        D[nr][nc] = D[r][c] + 1
                        S.append((nr,nc))
                        
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
max_distance = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            D = [[0]*m for _ in range(n)]
            D[i][j] = 1
            distance = 0
            bfs(i,j)
            if distance > max_distance:
                max_distance = distance
print(max_distance-1)