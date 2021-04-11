def bfs(S):
    while S:
        p = S.pop(0)
        r, c = p[0], p[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < height and nr > -1 and nc < width and nc > -1:
                if arr[nr][nc]:
                    arr[nr][nc] = 0 # 지나간 칸은 0으로
                    S.append((nr, nc))

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
            if arr[i][j]:
                S = [(i,j)]
                bfs(S)
                cnt += 1 # 1이 몇번 나오는지 세면 됨
    print(cnt)