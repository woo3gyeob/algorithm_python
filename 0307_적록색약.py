import copy
import sys
sys.setrecursionlimit(10**7) # 재귀 깊이를 10의 7제곱까지 늘려준다
def dfs(r, c): # 일반 사람의 구역을 산출하기 위한 dfs
    global flag1
    if arr[r][c] != '.':
        color = arr[r][c] # 조회한 좌표의 색깔 정보를 따로 저장
        arr[r][c] = '.'   # 조회한 좌표는 .으로 만든다
        flag1 = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < n: # 그림 밖으로 벗어나지 않는 좌표에 한해서
                if color == arr[nr][nc]:                    # 같은 색을 갖고 있는 다음 좌표를 탐색
                    dfs(nr, nc)
def dfs_rg(r, c): # 적록색약 사람의 구역을 산출하기 위한 dfs
    global flag2
    if arr2[r][c] != '.':
        color = arr2[r][c]
        arr2[r][c] = '.'
        flag2 = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < n and nc > -1 and nc < n:
                # 현재 좌표랑 색깔이 같거나, 둘 중 하나가 녹색, 다른 하나가 적색인 경우 하나의 구역으로 봐야 함
                if color == arr2[nr][nc] or (color == 'R' and arr2[nr][nc] == 'G') or (color == 'G' and arr2[nr][nc] == 'R'):
                    dfs_rg(nr, nc)
                    
n = int(input())
arr = [list(input()) for _ in range(n)]
arr2 = copy.deepcopy(arr) # 적록색약 사람의 구역 탐색을 위한 2차원 리스트 복사
cnt1, cnt2 = 0, 0 # 몇 구역인지 셀 변수
dr = [1,0,-1,0]
dc = [0,1,0,-1]
for i in range(n):
    for j in range(n):
        flag1, flag2 = False, False # 좌표가 .이 아니면 True로 바뀌고 구역을 탐색한다
        dfs(i, j)
        if flag1:   # 새로운 구역을 찾았으면 True로 바뀌게 설정
            cnt1 += 1
        dfs_rg(i, j)
        if flag2:
            cnt2 += 1
print(cnt1, cnt2)