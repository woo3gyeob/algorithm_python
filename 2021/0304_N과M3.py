def perm(idx):
    if idx == m:
        print(*sel)
        return
    else:
        for i in range(n): # 방문 안한 정점에 한해 조회할 필요 X
            sel[idx] = arr[i]
            perm(idx+1)
                
n, m = map(int, input().split())
sel = [0]*m
arr = list(range(1, n+1)) # 1 2 3 4
perm(0)

'''
중복이 가능한 순열
n = 4, m = 2 -> 방문체크할 필요 X. 모든 1 ~ n까지 가능한 m개의 수열
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
'''