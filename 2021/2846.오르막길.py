n = int(input())
ls = list(map(int, input().split())) + [0]
height = max_height = 0
cnt = i = 1
while i <= n:
    if ls[i] > ls[i-1]:
        cnt += 1
    else:
        if cnt >= 2:
            height = ls[i-1] - ls[i - cnt]
            if max_height < height:
                max_height = height
        cnt = 1
    i += 1
print(max_height)


'''
1 2 3 4 5 4 1 3 4 7 0
'''