def dfs(r,c):
    global cnt
    if arr[r][c] == 1:
        arr[r][c] = 0
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < n:
                if arr[nr][nc] == 1:
                    dfs(nr, nc)
        
n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
ls = []
for i in range(n):
    for j in range(n):
        cnt = 0
        dfs(i,j)
        if cnt != 0:
            ls.append(cnt)
print(len(ls))
ls.sort()
for i in range(len(ls)):
    print(ls[i])

'''
연결된 숫자 1 개수 세기
7
0 1 1 0 1 0 0
0 1 1 0 1 0 1
1 1 1 0 1 0 1
0 0 0 0 1 1 1
0 1 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 0 0 0
'''