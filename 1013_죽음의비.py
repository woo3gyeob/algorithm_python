# 백준 22944 죽음의 비
# https://www.acmicpc.net/problem/22944



from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

n, myEnergy, umbrellaDurability = map(int, input().split())
arr = []
sr, sc = 0, 0
for i in range(n):
    ls = list(input())
    for j in range(n):
        if ls[j] == 'S':
            sr, sc = i, j
    arr.append(ls)


def bfs():
    S = deque()
    S.append((sr,sc,myEnergy,0,0))
    visit = [[0]*n for _ in range(n)]
    visit[sr][sc] = 1

    while S:
        r, c, energy, umbrella, time = S.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if visit[nr][nc]: continue
            if arr[nr][nc] == '.':
                if umbrella == 0:
                    if energy == 0: continue
                    else: S.append((nr, nc, energy-1, umbrella, time+1))
                else:
                    S.append((nr, nc, energy, umbrella-1, time+1))
            elif arr[nr][nc] == 'U':
                S.append((nr, nc, energy, umbrellaDurability-1, time+1))
            elif arr[nr][nc] == 'E':
                return time+1

    return -1

print(bfs())


########################################

from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,h,d = map(int, input().split())
board = []

sx=sy=-1
for x in range(n):
    board.append(list(input().strip()))
    if sx==-1:
        for y in range(n):
            if board[x][y] == 'S':
                sx,sy = x,y

def solv():
    visited = [[0]*n for _ in range(n)]
    q = deque([(sx,sy,h,0,0)])
    visited[sx][sy] = h

    while q:
        x,y,now_h,now_d,cnt = q.pop()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if point_validator(nx,ny):
                if board[nx][ny] == 'E':
                    print(cnt+1)
                    return
                nxt_h = now_h
                nxt_d = now_d

                if board[nx][ny] == 'U':
                    nxt_d = d

                if nxt_d == 0:
                    nxt_h -= 1
                else:
                    nxt_d -= 1

                if nxt_h == 0:
                    continue

                if visited[nx][ny] < nxt_h:
                    visited[nx][ny] = nxt_h
                    q.appendleft((nx,ny,nxt_h,nxt_d,cnt+1))

    print(-1)


def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

solv()