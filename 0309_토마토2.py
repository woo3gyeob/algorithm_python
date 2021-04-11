# pypy3만 통과 python3는 시간초과
m, n, h = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(h)]
S = [0]*(m*n*h)
D = [[[0]*m for _ in range(n)] for _ in range(h)]
front = rear = 0
dr = [0,0,1,0,-1,0]
dc = [0,0,0,1,0,-1]
dk = [1,-1,0,0,0,0]
cnt = 0 # 0이 아닌 개수
day = 0 # 최소 일수
for k in range(h):
    for i in range(n):
        ls = list(map(int, input().split()))
        for j in range(m):
            if ls[j]: # 1 or -1
                cnt += 1
                if ls[j] == 1: # 1은 큐에 추가
                    S[rear] = (k,i,j)
                    rear += 1
        arr[k][i] = ls

while front != rear:
    point = S[front]
    front += 1
    k, r, c = point[0], point[1], point[2]
    if cnt == m*n*h: # 배열에 0이 없으면
        break
    for i in range(6):
        nk = k + dk[i]
        nr = r + dr[i]
        nc = c + dc[i]
        if nk > -1 and nk < h and nr > -1 and nr < n and nc > -1 and nc < m:
            if arr[nk][nr][nc] == 0:
                arr[nk][nr][nc] = 1
                D[nk][nr][nc] = D[k][r][c] + 1
                S[rear] = (nk,nr,nc)
                rear += 1
                cnt += 1
                if day < D[nk][nr][nc]: # 최소 일수 갱신
                    day = D[nk][nr][nc]
if cnt == m*n*h: # 0이 안남아있으면
    print(day)
else:
    print(-1)