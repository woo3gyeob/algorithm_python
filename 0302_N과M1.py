def perm(idx, target):
    if idx == target:
        if target == 1:
            print(sel[0])
        else:
            print(' '.join(list(map(str, sel))))
        return
    for i in range(n):
        if check[i] == 0:
            sel[idx] = arr[i]
            check[i] = 1
            perm(idx+1, target)
            check[i] = 0
            
n ,m = map(int, input().split())
arr = list(range(1, n+1))
sel = [0] * m
check = [0] * n
answer = []
perm(0, m)
