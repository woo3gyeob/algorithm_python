nums = list(map(int, input().split()))
for i in range(min(nums),10000000):
    cnt = 0
    for j in nums:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break
