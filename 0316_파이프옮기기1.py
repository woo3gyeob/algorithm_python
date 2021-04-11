# pypy3 87% 시간초과, python3 63% 시간초과
from collections import deque

def bfs(sr,sc,direction):
    global cnt
    S = deque()
    S.append((sr,sc))
    states = deque()
    states.append(direction)
    while S:
        point = S.popleft()
        state = states.popleft()
        r, c = point[0], point[1]
        if r == n-1 and c == n-1:
            cnt += 1
        else:
            for i in movable[state]:
                nr = r + dr[i]
                nc = c + dc[i]
                if nr > -1 and nr < n and nc > -1 and nc < n:
                    if not arr[nr][nc]:
                        if i == 2:
                            if not arr[r][nc] and not arr[nr][c]:
                                S.append((nr,nc))
                                states.append(i)
                        else:
                            S.append((nr,nc))
                            states.append(i)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [1,0,1]
dc = [0,1,1]
movable = [[0,2],[1,2],[0,1,2]]
cnt = 0
bfs(0,1,1)
print(cnt)