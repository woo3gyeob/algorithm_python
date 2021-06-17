n, m, time = map(int, input().split())
arr = []
bombs = []
for i in range(n):
    string = input()
    for j in range(m):
        if string[j] == 'O':
            bombs.append((i,j))
    arr.append(string)

dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 그냥 1초일 때
if time == 1:
    for i in range(n):
        print(arr[i])

# 짝수 초 후
elif not time % 2:
    all_bombs = 'O'*m
    for _ in range(n):
        print(all_bombs)

else:
    three = [['O']*m for _ in range(n)]
    for r, c in bombs:
        three[r][c] = '.'
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            three[nr][nc] = '.'

    one = [['O']*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if three[r][c] == 'O':
                one[r][c] = '.'
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
                    one[nr][nc] = '.'
    # 4n+1초 후
    if (time - 1) % 4 + 1 == 1:
        for i in range(n):
            print(''.join(one[i]))

    # 4n+3초 후
    elif (time - 1) % 4 + 1 == 3:
        for i in range(n):
            print(''.join(three[i]))

'''
1초일때와 4n+1초 후의 격자판이 왜 다른가?
-> 밑에 두개의 결과는 같다

6 7 5
.......
...O...
....O..
.......
OO.....
OO.....

6 7 5
.......
...O...
....O..
.......
OO.....
.O.....

'''