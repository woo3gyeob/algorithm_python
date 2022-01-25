# 백준 17212 달나라
# 33052KB / 184ms
# 1 2 5 7원

n = int(input())
dp = list(range(100001))

for i in range(2, n+1):
    dp[i] = min(dp[i-2]+1, dp[i])
    if i >= 5:
        dp[i] = min(dp[i-5]+1, dp[i])
    if i >= 7:
        dp[i] = min(dp[i-7]+1, dp[i])

print(dp[n])

