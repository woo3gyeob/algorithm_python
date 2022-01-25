# 백준 2580 스도쿠
# 135848KB, 1740ms
def is_possible(r,c,num):
    if num in arr[r]:
        return False
    for i in range(9):
        if num == arr[i][c]:
            return False
    sr, sc = r // 3, c // 3
    for i in range(sr*3, sr*3+3):
        for j in range(sc*3, sc*3+3):
            if num == arr[i][j]:
                return False
    return True

def perm(idx):
    if idx == end:
        for i in range(n):
            print(*arr[i])
        return 1
    r, c = S[idx]
    for i in range(1, 10):
        if is_possible(r,c,i):
            arr[r][c] = i
            if perm(idx+1) == 1: return 1
            arr[r][c] = 0

n = 9
arr = [list(map(int, input().split())) for _ in range(n)]
S = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            S.append((i,j))
end = len(S)
perm(0)