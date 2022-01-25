n, nation = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arr = sorted(arr, key = lambda x : (-x[1], -x[2], -x[3]))
for i in range(n):
    if nation == arr[i][0]:
        rank = i + 1
        for j in range(i-1,-1,-1):
            if arr[i][1:] == arr[j][1:]:
                rank -= 1
        print(rank)
        break