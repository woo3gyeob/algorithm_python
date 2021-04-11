import sys
sys.setrecursionlimit(10**7)
n, k = map(int, input().split())
def finding(a, cnt):
    if a == k:
        
        return 1
    if a <= k//2:
        return 1 + finding(2*a)
    if a > k:
        return 1 + finding(a-1)
    if k//2 < a < k:
        return 1 + finding(a+1)
        return 1 + finding(a-1)
min_val = 100001
cnt = finding(n)
print(cnt)



# 
from collections import deque

def bfs(a):
    global min_sec
    S = deque()
    S.append((a,0))
    while S:
        ls = S.popleft()
        subin, sec = ls[0], ls[1]
        if subin == k:
            if sec < min_sec:
                min_sec = sec
        if subin > k:
            S.append((subin-1,sec+1))
        elif subin <= k//2:
            S.append((2*subin, sec+1))
        else:
            S.append((2*subin, sec+1))
            S.append((subin-1, sec+1))
            S.append((subin+1, sec+1))

n, k = map(int, input().split())
min_sec = 987654321
bfs(n)