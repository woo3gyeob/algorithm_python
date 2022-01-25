# 백준 16954 움직이는 미로 탈출
# 31780KB 104ms
from collections import deque

arr = [list(input()) for _ in range(8)]
walls = deque()
for i in range(7,-1,-1):
    for j in range(8):
        if arr[i][j] == '#':
            walls.append((i,j))


S = deque([(7,0)])

dr = [0,1,0,-1,0,1,1,-1,-1]
dc = [0,0,1,0,-1,1,-1,-1,1]

wall_cnt = len(walls)
answer = 0
flag = False
while S:
    visit = [[0]*8 for _ in range(8)]
    for _ in range(len(S)):
        r, c = S.popleft()
        if arr[r][c] == '#': continue
        for i in range(9):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > 7 or nr < 0 or nc > 7 or nc < 0: continue
            if arr[nr][nc] == '#' or visit[nr][nc]: continue
            if nr == 0 and nc == 7:
                flag = True
            S.append((nr,nc))
            visit[nr][nc] = 1
    if flag:
        answer = 1
        break
    # print('후보들', S)
    for i in range(wall_cnt):
        r, c = walls.popleft()
        arr[r][c] = '.'
        nr = r + 1
        if nr > 7:
            wall_cnt -= 1
            continue
        arr[nr][c] = '#'
        walls.append((nr,c))
    # print('벽', walls)
    if wall_cnt <= 0 and S:
        answer = 1
        break
print(answer)