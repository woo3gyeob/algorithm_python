import sys
sys.setrecursionlimit(10**7) # 재귀 깊이를 10의 7제곱까지 늘려준다

def dfs(r, c): # 배추흰지렁이로 보호할 수 있는 좌표 1로 만들기 위함
    arr[r][c] = 0 # 조회한 칸은 0으로
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < height and nr > -1 and nc < width and nc > -1:
            if arr[nr][nc] == 1: # 상하좌우 조회
                dfs(nr, nc)

dr = [1,0,-1,0]
dc = [0,1,0,-1]
for _ in range(int(input())):
    width, height, n = map(int, input().split())
    arr = [[0]*width for _ in range(height)]
    for _ in range(n):
        c, r = map(int, input().split())
        arr[r][c] = 1
    cnt = 0
    for i in range(height):
        for j in range(width):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt += 1 # 배추밭에서 1을 찾은 횟수만 세면 됨
    print(cnt)