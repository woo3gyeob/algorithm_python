def perm(idx, j):
    if idx == m:
        print(*sel)
        return
    else:
        for i in range(j, n): # j는 직전의 i
            sel[idx] = arr[i]
            perm(idx+1, i)

n, m = map(int, input().split())
sel = [0] * m
arr = list(range(1, n+1))
perm(0, 0)

'''
원소간 중복은 허용이지만 순열간 중복은 허용되지 않는 순열 1 1 2
n = 3, m = 3
1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3
'''