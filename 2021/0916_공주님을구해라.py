# 백준 17836 공주님을 구해라!
# https://www.acmicpc.net/problem/17836
# 31940KB 104ms
import sys
input = sys.stdin.readline
from collections import deque

n, m, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
D = [[0]*m for _ in range(n)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
masterSord = 10000000

def bfs():
    global masterSord
    S = deque()
    S.append((0,0))
    while S:
        r, c = S.popleft()
        if D[r][c] > T:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= n or nr < 0 or nc >= m or nc < 0: continue
            if D[nr][nc]: continue
            if arr[nr][nc] == 2:
                D[nr][nc] = D[r][c] + 1 + (n-1) - nr + (m-1) - nc
                masterSord = D[nr][nc]
            if arr[nr][nc]==1: continue 
            D[nr][nc] = D[r][c] + 1
            if nr == n-1 and nc == m-1:
                return min(D[nr][nc], masterSord)
            S.append((nr,nc))
    
    return masterSord

answer = bfs()
if answer > T:
    print('Fail')
else:
    print(answer)
# print(bfs())
