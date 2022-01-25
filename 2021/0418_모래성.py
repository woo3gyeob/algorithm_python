# 백준 10711 모래성
# PyPy3 158800KB, 536ms
n, m = map(int, input().split())
S = []
arr = []
for i in range(n):
    ls = list(input())
    for j in range(m):
        if ls[j] == '.':
            S.append((i,j))
        else:
            ls[j] = int(ls[j])
    arr.append(ls)
            
delta = [(1,1),(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
wave = 0
while S:
    for _ in range(len(S)):
        r, c = S.pop(0)
        for i in range(8):
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if nr > -1 and nr < n and nc > -1 and nc < m:
                if arr[nr][nc] != '.':
                    arr[nr][nc] -= 1
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = '.'
                        S.append((nr,nc))
    wave += 1
print(wave-1)

# deque은 584ms