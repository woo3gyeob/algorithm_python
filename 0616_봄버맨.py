n, m, time = map(int, input().split())
one = []
bombs = []
for i in range(n):
    string = input()
    for j in range(m):
        if string[j] == 'O':
            bombs.append((i,j))
    one.append(string)

dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 짝수 초 후
if not time % 2:
    all_bombs = 'O'*m
    for _ in range(n):
        print(all_bombs)
        
# 4n+1초 후
elif (time - 1) % 4 + 1 == 1:
    for i in range(n):
        print(one[i])

# 4n+3초 후
elif (time - 1) % 4 + 1 == 3:
    three = [['O']*m for _ in range(n)]
    for r, c in bombs:
        three[r][c] = '.'
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            three[nr][nc] = '.'
    for i in range(n):
        print(''.join(three[i]))
