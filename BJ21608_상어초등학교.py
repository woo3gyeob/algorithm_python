############## 29200 KB / 316 ms ###############
n = int(input())

# 첫번째 친구 먼저 받아옴
ls = list(map(int, input().split()))
first_stu = ls.pop(0)
like_stus = {}              # 좋아하는 친구 리스트는 딕셔너리로 저장
like_stus[first_stu] = ls

stus = []

# 두번째 친구 ~ 마지막친구 받아옴
for i in range(n*n-1):
    ls = list(map(int, input().split()))
    stu = ls.pop(0)
    stus.append(stu)
    like_stus[stu] = ls

dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 배치 -> 첫 친구는 1,1에 넣을거임
arr = [[0]*n for _ in range(n)]
arr[1][1] = first_stu


# 두번째 친구부터 배치 시작
for stu in stus:
    r, c, maxFriends, maxBlanks = 0, 0, -1, -1  # 자꾸 keyError 발생한 원인!
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0: continue
            friends = 0
            blanks = 0
            for d in range(4):
                ni = i + dr[d]
                nj = j + dc[d]
                if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                if arr[ni][nj] == 0: blanks += 1
                elif arr[ni][nj] in like_stus[stu]: friends += 1

            if friends > maxFriends:
                maxFriends = friends 
                maxBlanks = blanks
                r, c = i, j
            elif friends == maxFriends and blanks > maxBlanks: 
                maxBlanks = blanks
                r, c = i, j

    # (r,c)에 배치
    arr[r][c] = stu

# 만족도 계산
satisfied = 0
for i in range(n):
    for j in range(n):
        stu = arr[i][j]
        point = 0
        for d in range(4):
            ni = i + dr[d]
            nj = j + dc[d]
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            if arr[ni][nj] in like_stus[stu]: 
                point += 1
        # 만족도 누적 합산
        if point == 0: continue
        else: satisfied += 10 ** (point-1)

print(satisfied)

