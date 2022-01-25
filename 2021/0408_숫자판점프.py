# 백준 2210
# 29800KB, 96ms
def perm(r, c, idx):
    if idx == 6:
        nums.add(''.join(sel))
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr > -1 and nr < 5 and nc > -1 and nc < 5:
            sel[idx] = arr[nr][nc]
            perm(nr, nc, idx+1)

arr = [input().split() for _ in range(5)]
sel = [0]*6
dr = [0,1,0,-1]
dc = [1,0,-1,0]
nums = set()
for i in range(5):
    for j in range(5):
        perm(i, j, 0)
print(len(nums))

#########################################
# 29800KB, 72ms
def perm(r, c, string):
    string += arr[nr][nc]
    if len(string) == 6:
        nums.add(string)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr > -1 and nr < 5 and nc > -1 and nc < 5:
            perm(nr, nc, string)

arr = [input().split() for _ in range(5)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
nums = set()
for i in range(5):
    for j in range(5):
        perm(i, j, '')
print(len(nums))