# 백준 2206
# https://www.acmicpc.net/problem/2206

# 3차원으로 풀어?
from collections import deque

def bfs(sr,sc,sflag):
    S = deque()
    S.append((sr,sc,sflag))
    while S:
        point = S.popleft()
        r, c, z = point[0], point[1], point[2]
        if r == n-1 and c == m-1:
            return visited[r][c][z]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < m:
                if not arr[nr][nc] and not visited[nr][nc][z]:
                    visited[nr][nc][z] = visited[r][c][z] + 1
                    S.append((nr,nc,z))
                elif not z and arr[nr][nc] and not visited[nr][nc][1]:
                    visited[nr][nc][1] = visited[r][c][z] + 1
                    S.append((nr,nc,1))
    return -1

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
visited = [[[0]*2 for _ in range(m)]for _ in range(n)]
visited[0][0][0] = 1
print(bfs(0,0,0))

