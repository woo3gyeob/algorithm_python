# 백준 11265 끝나지 않는 파티
# https://www.acmicpc.net/problem/11265
# PyPy3 130436KB / 3660ms 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(party, time):
    if time < 0:
        return
    if party == target:
        return True
    for i in range(n):
        if visit[i]: continue
        visit[i] = 1
        ret = dfs(i, time - arr[party][i])
        visit[i] = 0
        if ret: return ret
    return False

for _ in range(m):
    start, target, time = map(int, input().split())
    start -= 1
    target -= 1
    visit = [0]*n
    visit[start] = 1
    result = dfs(start, time)
    if result: print("Enjoy other party")
    else: print("Stay here")

