# pypy3  152804KB, 3968ms
def dfs(cnt):
    global answer
    if cnt == n * m:
        answer += 1
        return
    r = cnt // m
    c = cnt % m
    if r >= n or c >= m: return
    if arr[r-1][c] == 1 and arr[r][c-1] == 1 and arr[r-1][c-1] == 1:
        dfs(cnt+1)
    else:
        dfs(cnt+1)
        arr[r][c] = 1
        dfs(cnt+1)
        arr[r][c] = 0

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
answer = 0
dfs(0)
print(answer)