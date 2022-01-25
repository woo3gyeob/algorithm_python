# 백준 5427
from collections import deque

def bfs(point):
    S = deque([point])
    while S:
        for _ in range(len(fire)):      # 불 1칸씩 우선 번지게 해줌
            fp = fire.popleft()
            fr, fc = fp[0], fp[1]
            for i in range(4):
                nfr = fr + dr[i]
                nfc = fc + dc[i]
                if nfr > -1 and nfr < n and nfc > -1 and nfc < m:
                    if arr[nfr][nfc] == '.' or arr[nfr][nfc] == '@': # 빈공간(.)하고 상근이 위치(@)도 불 번질 수 있다!
                        arr[nfr][nfc] = '*'
                        fire.append((nfr,nfc))
        for _ in range(len(S)):                                      # 불이 번지고 난 다음 이동할 있는 곳으로 상근이 1칸 이동
            p = S.popleft()
            r, c = p[0], p[1]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if arr[nr][nc] == '.':                               # 위/아래/우/좌 방향 중 빈공간인 부분만 갈 수 있음
                    if nr == n-1 or nr == 0 or nc == m-1 or nc == 0: # 인덱스 범위 끝(판 가장자리)에 오면
                        return arr[r][c] + 1                         # 직전 위치까지의 거리 + 1해서 리턴
                    else:
                        arr[nr][nc] = arr[r][c] + 1                  # 거리 1씩 늘려줌
                        S.append((nr,nc))
    return "IMPOSSIBLE"                                              # 인덱스 범위 끝까지 못가면 impossible 리턴

dr = [1,0,-1,0]
dc = [0,1,0,-1]

for tc in range(int(input())):
    m, n = map(int, input().split())
    arr = []
    fire = deque()
    for i in range(n):
        ls = list(input())
        for j in range(m):
            if ls[j] == '*':
                fire.append((i,j))      # 불 위치를 저장해야 한다
            elif ls[j] == '@':
                start = (i,j)           # 상근이의 첫 위치
        arr.append(ls)
    if start[0] == n-1 or start[0] == 0 or start[1] == m-1 or start[1] == 0: # 위 bfs는 출발점이 가장자리면 연산범위를 벗어남 
        print(1)
    else:
        arr[start[0]][start[1]] = 1     # 첫 위치의 거리를 1로 설정
        print(bfs(start))


'''
2번 예제
# # # @ # # #
# * # 4 # * #
# f f 3 f f #
# f 3 2 3 f #
# 3 2 1 2 3 #
# # # # # # #
위 코드 돌리고 난 후 arr 상태
''arr
# # # . # # #
# * # 4 # * #
# * * 3 * * #
# * 3 2 3 * #
# 3 2 1 2 3 #
# # # # # # #
''
'''