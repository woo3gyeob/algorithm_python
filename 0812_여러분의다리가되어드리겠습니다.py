# 백준 17352
# https://www.acmicpc.net/problem/17352
# 88324KB, 1136ms

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-2):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visit = [0]*(n+1)
visit[1] = 1
S = deque([1])

while S:
    node = S.popleft()
    for i in arr[node]:
        if not visit[i]:
            visit[i] = 1
            S.append(i)

answer = 0
for i in range(1, n+1):
    if not visit[i]:
        answer = i
        break

print('1 %d' %(answer))