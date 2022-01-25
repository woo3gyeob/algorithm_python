# 백준 1890 점프
# https://www.acmicpc.net/problem/1890

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)] # 지나온 횟수를 저장하는 2차원 배열
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        # 오른쪽 맨아래 도달
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
        how_many_to_go = arr[i][j]
        # 오른쪽 이동
        if j + how_many_to_go < n:
            dp[i][j + how_many_to_go] += dp[i][j]
        # 아래쪽 이동
        if i + how_many_to_go < n:
            dp[i + how_many_to_go][j] += dp[i][j]