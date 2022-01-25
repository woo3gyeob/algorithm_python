# 시간초과
# import sys

# n = int(input())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# arr.sort(key=lambda x : x[0])

# end_time = [arr[0][1]]
# for i in range(1, n):
#     if arr[i][0] >= min(end_time):
#         end_time.remove(min(end_time))
#     end_time.append(arr[i][1])

# print(len(end_time))


#####
import heapq
import sys

N = int(input())

timeTable = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue,timeTable[0][1])

for i in range(1,N):
    if queue[0] > timeTable[i][0]:
        heapq.heappush(queue,timeTable[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,timeTable[i][1])

print(len(queue))