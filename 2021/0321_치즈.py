# 백준 2636 치즈
import sys
sys.setrecursionlimit(10**7)

def dfs(point):
    global num_of_1
    r, c = point[0], point[1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr > -1 and nr < n and nc > -1 and nc < m:
            if not visited[nr][nc]: # 방문을 안했으면 방문 체크
                visited[nr][nc] = 1
                if arr[nr][nc]:     # 1(치즈)일때
                    arr[nr][nc] = 0 # 1인 애들은 0으로 만들고 재귀는 돌지 않는다
                    num_of_1 += 1   # 1 개수 세기
                else:
                    dfs((nr,nc)) # 0일 때만 재귀
    
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [1,0,-1,0]
dc = [0,1,0,-1]
total = []
hours_all_melted = 0
while True:
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1           # (0,0)부터 dfs 탐색
    num_of_1 = 0                # 한 번 dfs 돌 때마다 1 개수를 셀거임
    dfs((0,0))
    if not num_of_1:            # 1이 하나도 없다 = 치즈가 다 녹았다
        num_of_1 = total[-1]    # 직전의 1의 개수를 저장하고 while문 빠져나오기
        break
    hours_all_melted += 1       # 치즈가 남아있으면 시간을 1씩 늘려줌
    total.append(num_of_1)      # 해당 iter에서 계산한 1의 개수를 total 리스트에 저장
    
print(hours_all_melted)
print(num_of_1)

'''
# 0인 경우만 dfs 탐색 (예시: 7x7, 1=치즈, 0=빈공간)
# 초기 arr = 
0 0 0 0 0 0 0
0 1 1 1 1 1 0       # arr[1][1] = 1이므로 재귀는 타지 않지만, 0으로 값 치환되고 visited에 방문 체크!
0 1 1 1 1 1 0       # 방문 체크했으므로 값은 0으로 바뀌어도 dfs 재귀를 타지 않음
0 1 1 0 1 1 0       # 그렇게 0인 테두리 안의 한 겹의 층의 치즈(1)만 값을 0으로 바꾸고 다음 while문에 활용할 수 있음!
0 1 1 1 1 1 0       # visited는 while 반복문을 돌 때마다 초기화되므로 기존에 치즈(1)였다가 0으로 바뀐 좌표도 다시 탐색 가능!
0 1 1 1 1 1 0
0 0 0 0 0 0 0

# 1차 dfs 후 visited = 
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 0 0 0 1 1
1 1 0 0 0 1 1
1 1 0 0 0 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1

# 1차 dfs 후 arr =
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 1 1 1 0 0
0 0 1 0 1 0 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
'''