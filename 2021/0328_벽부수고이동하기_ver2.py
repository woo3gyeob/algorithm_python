# 마지막까지 발악한 코드
from collections import deque

def bfs(sr,sc,sflag):
    S = deque()
    S.append((sr,sc,sflag))
    while S:
        point = S.popleft()
        r, c, flag = point[0], point[1], point[2]
        if r == n-1 and c == m-1:
            return visited[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < m:
                if arr[nr][nc] == 1 and not flag:
                    visited[nr][nc] = visited[r][c] + 1
                    S.append((nr,nc,True))
                elif arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    S.append((nr,nc,flag))
    return -1
    
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
visited = [[0]*m for _ in range(n)]     # visited를 왜 3차원으로 써야 하는가
visited[0][0] = 1
print(bfs(0,0,False))

'''
3차원 visited

[[[1, 0], [2, 0], [3, 0], [4, 0]],
 [[0, 0], [0, 3], [0, 0], [5, 0]],
 [[0, 0], [8, 4], [7, 0], [6, 0]],
 [[0, 0], [0, 5], [0, 8], [0, 0]],
 [[0, 0], [0, 6], [0, 7], [0, 0]]]
'''

'''
arr
0000
1110
1000
0011
0010

visited
1100
0100
0100
0100
0110
'''