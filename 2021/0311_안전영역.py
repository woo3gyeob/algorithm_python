import copy

def bfs(r, c, h):
    S = [(r,c)]
    while S:
        point = S.pop(0)
        r, c = point[0], point[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < n:
                if arr2[nr][nc] > h:
                    arr2[nr][nc] = 0
                    S.append((nr,nc))
                    
n = int(input())
arr = []
numbers = set()
for i in range(n):
    ls = list(map(int, input().split()))
    for j in range(n):
        numbers.add(ls[j])
    arr.append(ls)

dr = [1,0,-1,0]
dc = [0,1,0,-1]
max_area = 0
for height in numbers:
    arr2 = copy.deepcopy(arr)
    area = 0
    for i in range(n):
        for j in range(n):
            if arr2[i][j] > height:
                arr2[i][j] = 0
                area += 1
                bfs(i,j,height)
    if area > max_area:
        max_area = area
if max_area == 0:
    print(1)
else:
    print(max_area)