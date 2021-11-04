# 백준 1600 말이 되고픈 원숭이
from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

hr = [-2,-1,1,2,2,1,-1,-2]
hc = [-1,-2,-2,-1,1,2,2,1]

def bfs():
    sr, sc = 0, 0
    visit = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    S = deque()
    S.append((sr,sc,k))
    while S:
        r, c, kk = S.popleft()
        if r == h-1 and c == w-1:
            return visit[r][c][kk]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
            if visit[nr][nc][kk] or arr[nr][nc]: continue
            visit[nr][nc][kk] = visit[r][c][kk] + 1
            S.append((nr,nc,kk))

        if kk > 0:
            for i in range(8):
                nr = r + hr[i]
                nc = c + hc[i]
                if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
                if visit[nr][nc][kk-1] or arr[nr][nc]: continue
                visit[nr][nc][kk-1] = visit[r][c][kk] + 1
                S.append((nr,nc,kk-1))
    return -1
print(bfs())