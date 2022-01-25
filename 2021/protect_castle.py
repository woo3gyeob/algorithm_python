m, n = map(int, input().split())
row = [False]*m     # 행에서 X가 있는 인덱스는 True로 바꿔줄 거임
col = [False]*n     # 열에서 X가 있는 인덱스는 True로 바꿔줄 거임
for i in range(m):
    guard = input()
    if 'X' in guard:
        row[i] = True
    for j in range(n):
        if guard[j] == 'X':
            col[j] = True

print(max([m-sum(row), n-sum(col)]))


'''
col
 FFTT
...X  T  c
..X.  T  o
....  F  l
..XX  T 

m, n = 4, 4
sum(row) = 2
sum(col) = 3

max(4-2, 4-3) = 2
'''