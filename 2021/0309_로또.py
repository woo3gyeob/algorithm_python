def perm(idx, start):
    if idx == 6:
        print(*sel)
    else:
        for i in range(start, k):
            if not checked[i]:
                sel[idx] = ls[i]
                checked[i] = 1
                perm(idx+1, i+1)
                checked[i] = 0

while True:
    ls = list(map(int, input().split()))
    if ls[0] == 0:
        break
    k = ls.pop(0) # 맨 앞은 숫자 개수이므로 pop해서 빼줌
    checked = [0]*k
    sel = [0]*6
    perm(0, 0)
    print()