n, k = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
max_length = 0
while (n-i) > max_length:
    starts = [0]*100001
    dic = {}
    for j in range(i, n):
        num = arr[j]
        if starts[num] == 0:
            starts[num] = j+1
        dic[num] = dic.get(num, 0) + 1
        if dic[num] > k:
            if (j-i) > max_length:
                max_length = j-i
            i = starts[num]
            break
    if max_length == 0:
        max_length = n
        break
print(max_length)

# import sys

# n, k = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

# startIndex, maxCount = (0, 0)
# cnt = [0]*100001
# for i in range(len(arr)):
#     num = arr[i]
#     cnt[num] = cnt[num] + 1
#     if cnt[num] > k:
#         maxCount = max(maxCount, i-startIndex)
#         while(cnt[num] > k):
#             cnt[arr[startIndex]] = cnt[arr[startIndex]] - 1
#             startIndex += 1
#     else:
#         maxCount = max(maxCount, i-startIndex+1)
# print(maxCount)
