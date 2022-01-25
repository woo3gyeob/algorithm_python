def row_search(i, j, t):           # 행(가로) 탐색. t = 찾고자 하는 돌 번호 (1 or 2)
    global winner, r, c
    if sum([table[i][j + k] == t for k in range(5)]) == 5: # 찾고자 하는 돌이 5개 연속으로 있는지 합으로 찾음
        if table[i][j+5] != t and table[i][j-1] != t:      # 6목은 안되므로 딱 5개만 있는지 조회
            winner, r, c = t, i, j
def col_search(i,j,t):             # 열(세로) 탐색
    global winner, r, c
    if sum([table[i + k][j] == t for k in range(5)]) == 5:
        if table[i + 5][j] != t and table[i - 1][j] != t:
            winner, r, c = t, i, j
def slash_search(i,j,t):           # 우하향 대각선 탐색
    global winner, r, c
    if sum([table[i + k][j + k] == t for k in range(5)]) == 5:
        if table[i+5][j+5] != t and table[i-1][j-1] != t:
            winner, r, c = t, i, j
def reversed_slash_search(i,j,t):  # 우상향 대각선 탐색
    global winner, r, c
    if sum([table[i - k][j + k] == t for k in range(5)]) == 5:
        if table[i-5][j+5] != t and table[i+1][j-1] != t:
            winner, r, c = t, i, j
table = []
table.append([0]*21)
for _ in range(19):
    ls = [0] + list(map(int, input().split())) + [0] # 0으로 1차 패딩. 실제 값 인덱스 범위 0~19 ->  (1 ~ 20)
    table.append(ls)
table.append([0]*21)
winner, r, c = 0, 0, 0
for i in range(1, 20):
    if winner != 0:
        break
    for j in range(1, 20):
        if table[i][j] == 1:
            if j <= 15:              # 가로 탐색 시작점은 15번째까지 가능
                row_search(i, j, 1)
            if i <= 15:              # 세로 탐색 시작점은 15번째까지 가능
                col_search(i, j, 1)
            if i <= 15 and j <= 15: # 우하향 대각선 탐색 시작점은 행, 열 15번째까지 가능
                slash_search(i, j, 1)
            if i >= 5 and j <= 15:  # 우상향 대각선 탐색 시작점은 행은 5번째부터, 열은 15번째까지 가능
                reversed_slash_search(i,j,1)
        elif table[i][j] == 2:
            if j <= 15:
                row_search(i, j, 2)
            if i <= 15:
                col_search(i, j, 2)
            if i <= 15 and j <= 15:
                slash_search(i, j, 2)
            if i >= 5 and j <= 15:
                reversed_slash_search(i,j,2)

print(winner)
if winner != 0:
    print(r, c)

'''
0 ~ 21
0 21 = 0
1 ~ 20 
15 16 17 18 19
 1 1 1 1 1

0 0 0 0 0 0 0 0 ..
.... 0 1 1 1 1 1 0
0 0 0 1 1 1 1 1 1
1 1 1 11 1 1 11 1
11 11 1 11 1 1 11 1
'''
