from collections import deque

dr = [-1,0,1,1,0,-1]
doc = [0,-1,0,1,1,1]
dec = [-1,-1,-1,0,1,0]

m, n = map(int, input().split())
arr = []
arr.append([0]*(m+2))
for _ in range(n):
    ls = [0] + list(map(int, input().split())) + [0]
    arr.append(ls)
arr.append([0]*(m+2))

S = deque([(0,0)])

while S:
    r, c = S.popleft()
    for i in range(6):
        nr = r + dr[i]
        if c % 2 == 1:
            nc = c + doc[i]
        else:
            nc = c + dec[i]
        if arr[nr][nc] == 0:
            arr[nr][nc] = -1
            S.append((nr,nc))

wall_len = 0
arr.pop(0)


def dfs(r, c):
    global wall_len
    