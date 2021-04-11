a, b = input().split()
n, m = len(b), len(a) # n 행, m 열
arr = [['.']*m for i in range(n)]
pos_a, pos_b = None, None
for i in range(m):
    for j in range(n):
        if a[i] == b[j]:
            pos_b = i
            pos_a = j
            break
    if pos_a is not None:
        break
for i in range(m):
    arr[pos_a][i] = a[i]
for i in range(n):
    arr[i][pos_b] = b[i]
for i in range(n):
    print(''.join(arr[i]))