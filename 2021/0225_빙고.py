bingo = []
for _ in range(5):
    ls = list(map(int, input().split()))  # 내 빙고 리스트
    bingo.append(ls)
calls = []
for _ in range(5):
    calls += list(map(int, input().split()))  # 부르는 번호 리스트
row, col, diag = [], [], [] # 빙고가 된 인덱스 저장할 리스트
cnt = 0                     # 몇 빙고인지 카운트
for idx in range(25):
    for i in range(5):
        for j in range(5):
            if calls[idx] == bingo[i][j]: # 부르는 번호에 해당하는 내 빙고 숫자는 0으로 
                bingo[i][j] = 0           # 빙고인 행, 열, 대각선 원소의 합은 0이 될 것
                break
    if idx >= 11:                         # 최소 12번 이상은 불러야 3빙고가 되므로 12번째 수부터 조회 시작
        for i in range(5):
            if sum(bingo[i]) == 0 and i not in row: # 전부 0이다 = 빙고다, row에 없다 = 아직 빙고가 안된 줄이다
                cnt += 1
                row.append(i)
            if sum([bingo[j][i] for j in range(5)]) == 0 and i not in col:
                cnt += 1
                col.append(i)
        if sum([bingo[j][4-j] for j in range(5)]) == 0 and 1 not in diag: # 우상향 대각선 인덱스를 임의로 1로 설정
            cnt += 1
            diag.append(1)
        if sum([bingo[j][j] for j in range(5)]) == 0 and 2 not in diag:   # 우하향 대각선 인덱스를 임의로 2로 설정
            cnt += 1
            diag.append(2)

        if cnt >= 3:
            print(idx+1)
            break

'''
1 0 3 4 5
6 0 8 2 3
0 0 0 0 0
1 0 1 1 1
1 0 0 0 0
'''