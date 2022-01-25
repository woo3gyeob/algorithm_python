def moving(chess, mov):
    k = chess[:]              # 킹이나 돌이 판 밖으로 나가면 원위치 시키기 위한 변수 할당
    if 'R' in mov:            # 오른쪽으로 이동
        if ord(k[0]) <= 71:
            k[0] = chr(ord(k[0]) + 1)
        else:
            return chess
    if 'L' in mov:            # 왼쪽 이동
        if ord(k[0]) >= 66:
            k[0] = chr(ord(k[0]) - 1)
        else:
            return chess
    if 'T' in mov:            # 위로 이동
        if int(k[1]) <= 7:
            k[1] = str(int(k[1]) + 1)
        else:
            return chess
    if 'B' in mov:            # 아래로 이동
        if int(k[1]) >= 2:
            k[1] = str(int(k[1]) - 1)
        else:
            return chess
    return k
    
king, stone, n = input().split()
king = list([king[0], king[1]])
stone = list([stone[0], stone[1]])
n = int(n)
for _ in range(n):
    move = input()
    king_new = moving(king, move)       # 킹이 이동할 새로운 위치를 새로운 변수에 할당
    if king_new == stone:               # 킹이 이동한 위치와 돌의 위치가 같을 때
        stone_new = moving(stone, move) # 우선 똑같이 이동시킨 돌의 위치를 새로운 변수에 할당
        if stone_new != stone:          # 근데 새로운 돌의 위치가 판 밖으로 나가는 경우라면
            king = king_new[:]          # 킹과 돌 둘다 원위치
            stone = stone_new[:]
    else:                               # 킹이 이동해도 돌이랑 위치가 같지 않으면
        king = king_new[:]              # 입력대로 킹 이동
print(''.join(king))
print(''.join(stone))