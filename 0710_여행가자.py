# 29200KB, 2476ms
import sys

def dfs(start):
    global result
    if start == target:
        result = True
        return
    for i in range(n):
        if arr[start][i] == 0: continue
        if visit[i]: continue
        visit[i] = 1
        dfs(i)

n = int(input())
m = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
plan = list(map(int, sys.stdin.readline().split()))

for i in range(m-1):
    start = plan[i] - 1
    target = plan[i+1] - 1
    visit = [0]*n
    visit[start] = 1
    result = False
    dfs(start)
    if not result:
        print('NO')
        break
else:
    print('YES')