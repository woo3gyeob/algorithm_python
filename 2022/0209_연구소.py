# 백준 14502 연구소
# https://www.acmicpc.net/problem/14502
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
arr = []
candidates = []
virus = []
for i in range(n):
    ls = list(map(int, input().split()))
    for j in range(m):
        if ls[j] == 0:
            candidates.append((i, j))
        elif ls[j] == 2:
            virus.append((i, j))
    arr.append(ls)

# 3개씩 후보 좌표 산출
sel = [0] * 3
can_len = len(candidates)
max_safe_area = 0

def perms(idx, start):
    global max_safe_area
    if idx == 3:
        area = bfs()
        if area > max_safe_area:
            max_safe_area = area
        return
    
    for i in range(start, can_len):
        sel[idx] = candidates[i]
        perms(idx + 1, i + 1)
    
# 바이러스 퍼지기
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs():
    S = deque(virus)
    arr2 = deepcopy(arr)

    for r, c in sel:
        arr2[r][c] = 1

    while S:
        r, c = S.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if arr2[nr][nc]: continue
            arr2[nr][nc] = 2
            S.append((nr, nc))
    
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 0:
                safe_area += 1

    return safe_area

perms(0, 0)

print(max_safe_area)