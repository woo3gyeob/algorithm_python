# # https://www.acmicpc.net/problem/11403
# # 백준 11403 경로찾기

# def dfs(node, cnt, ls):
#     flag = False
#     for i in range(n):
#         if not visit[i] and arr[node][i]:
#             flag = True
#             visit[i] = 1
#             answer[node][i] = 1
#             answer[i][node] = 1
#             dfs(i, cnt + 1, ls+[i])
#             visit[i] = 0
#     if not flag:
#         for l in ls:
#             print(ls)
#             if arr[l][ls[0]]:
#                 answer[l][ls[0]] = 1
#                 answer[ls[0]][l] = 1
#         return

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# answer = [[0]*n for _ in range(n)]
# visit = [0]*n
# dfs(0, [0])
# for i in range(n):
#     print(*answer[i])

# ------------------------------------------------

# def find_path(node, target):
#     for i in range(n):
#         if arr[node][i]:
#             visit[node][i] = 1
#             visit[i][node] = 1
#             if i == target: return
#             find_path(i, target)
#             visit[node][i] = 0
#             visit[i][node] = 0


# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# answer = [[0]*n for _ in range(n)]
# visit = [0]*n
# for i in range(n-1):
#     for j in range(i+1, n):
        
#         if find_path(i,j):
#             answer[i][j] = 1
# for i in range(n):
#     print(*answer[i])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

#플로이드-워셜 알고리즘
for k in range(n): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1

for i in range(n):
    print(*arr[i])
