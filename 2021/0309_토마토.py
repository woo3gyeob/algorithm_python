m, n = map(int, input().split())
arr = []
S = [0] * (n*m) # 큐
rear = front = -1
dr = [1,0,-1,0]
dc = [0,1,0,-1]
D = [[0]*m for _ in range(n)]
day = 0 # 며칠 지났는지 셀 변수
cnt = 0 # 배열에서 0이 아닌 숫자를 셀 변수
for i in range(n):
    ls = list(map(int, input().split()))
    for j in range(m):
        if ls[j] != 0: # 1 or -1
            cnt += 1
            if ls[j] == 1: # 1이면 큐에 추가
                rear += 1
                S[rear] = (i,j)
    arr.append(ls)

while front != rear: # 공백되기 전가지 진행
    front += 1
    point = S[front]
    r, c = point[0], point[1]
    if cnt == m * n: # 배열에 0이 없으면 종료
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr > -1 and nr < n and nc > -1 and nc < m:
            if not arr[nr][nc]: # 값이 0일때
                cnt += 1
                arr[nr][nc] = 1
                D[nr][nc] = D[r][c] + 1
                rear += 1
                S[rear] = (nr,nc)
                if D[nr][nc] > day: # 최소 일수 갱신
                    day = D[nr][nc]
if cnt != m * n: # 배열에 0이 남아있는 경우
    print(-1)
else:
    print(day)