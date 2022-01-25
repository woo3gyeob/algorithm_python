# bfs 활용 32820KB, 316ms
from collections import deque

def dfs(a,b):       # 영역을 2 이상의 수로 채우기 위한 함수
    global fill_num
    S = deque([(a,b)])
    while S:
        p = S.popleft()
        r, c = p[0], p[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < n:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = fill_num
                    S.append((nr,nc))

def bfs(r,c):       # 영역을 연결하는 다리의 길이를 구하는 함수
    global min_distance, self_num
    S = deque([(r,c)])
    while S:
        p = S.popleft()
        r, c = p[0], p[1]
        if visited[r][c] > min_distance:                    # 이미 최소 거리를 넘었으면 더 볼 필요 없다
            return 10000
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < n:   
                if not arr[nr][nc] and not visited[nr][nc]: # 값이 0 이면서 + 아직 방문 안한 위치
                    visited[nr][nc] = visited[r][c] + 1     # visited는 거리 + 방문여부 한 번에 사용
                    S.append((nr, nc))
                elif arr[nr][nc] != self_num and arr[nr][nc] != 0 and not visited[nr][nc]:    # self_num은 자신의 영역 번호 
                    return visited[r][c] - 1                # 0과 자신의 영역번호 이외의 영역을 만나면 다리가 연결된 것이므로 그 거리를 리턴
    return 10000

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
min_distance = 10000

fill_num = 2                        # fill_num은 영역을 구별하기 위해 채울 번호 (2부터 시작)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:          
            arr[i][j] = fill_num    
            dfs(i,j)                # 한 영역은 같은 영역번호를 가짐
            fill_num += 1           # 새로운 영역을 발견할 때마다 1씩 커진 영역번호를 영역 전체에 할당

for i in range(n):
    for j in range(n):
        if arr[i][j]:               # 0 이외의 수만 조회
            flag = False
            for k in range(4):      # 주변에 0도 없는데 굳이 bfs함수 탈 필요가 없으므로 주변에 0 있는지 조회
                ni = i + dr[k]
                nj = j + dc[k]
                if ni > -1 and ni < n and nj > -1 and nj < n:
                    if arr[ni][nj] == 0:
                        flag = True
                        break
            if flag:                # 주변에 0 있을 때만 bfs 들어감
                visited = [[0]*n for _ in range(n)]
                visited[i][j] = 1
                self_num = arr[i][j]
                distance = bfs(i,j)
                if distance < min_distance:
                    min_distance = distance
print(min_distance)