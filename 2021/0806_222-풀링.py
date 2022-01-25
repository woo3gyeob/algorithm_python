# 백준 17829 222-풀링
# https://www.acmicpc.net/problem/17829
# 70516KB, 636ms

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def pooling(k, lr, hr, lc, hc):
    if k == 2:
        ls = [arr[lr][lc], arr[lr+1][lc], arr[lr][lc+1], arr[lr+1][lc+1]]
        ls.sort()
        second = ls[2]
        return second
    
    mr = (lr + hr) // 2
    mc = (lc + hc) // 2
    k = k//2
    lst = sorted([pooling(k, lr, mr, lc, mc), pooling(k, mr, hr, lc, mc), pooling(k, lr, mr, mc, hc), pooling(k, mr, hr, mc, hc)])
    second_value = lst[2]
    return second_value
    

answer = pooling(n, 0, n, 0, n)
print(answer)