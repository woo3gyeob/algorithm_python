def perm(idx, target, j):
    if idx == target:
        if target == 1:
            print(sel[0])
        else:
            print(' '.join(list(map(str, sel))))
        return
    for i in range(j, n): # j는 직전의 i+1
        if check[i] == 0:
            sel[idx] = arr[i]
            check[i] = 1
            perm(idx+1, target, i+1)
            check[i] = 0

n ,m = map(int, input().split())
arr = list(range(1, n+1))
sel = [0] * m
check = [0] * n
perm(0, m, 0)

'''
1 2
1 3
1 4 -> 1이 이미 방문했다X 2
2 3
2 4
3 4
n, m = 4, 2
i = 0  ->   1 ~ 3
i = 1  ->   2 ~ 3
i = 2 ->    3 ~ 3
'''