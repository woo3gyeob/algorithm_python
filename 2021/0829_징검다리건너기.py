# 백준 21317 징검다리건너기
# https://www.acmicpc.net/problem/21317

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n-1)]
k = int(input())
D = [0xffffff] * n
D[0] = 0
veryBigJump = False
def jump(idx):
    global veryBigJump
    if idx == n-1:
        # print(D)
        return
    # if idx > n-1:
    #     return
    if D[idx+1] > D[idx] + arr[idx][0]:
        D[idx+1] = D[idx] + arr[idx][0]
        jump(idx+1)
    if idx+2 <= n-1:
        if D[idx+2] > D[idx] + arr[idx][1]:
            D[idx+2] = D[idx] + arr[idx][1]
            jump(idx+2)
    if idx+3 <= n-1:
        if not veryBigJump and D[idx+3] > D[idx] + k:
            D[idx+3] = D[idx] + k
            veryBigJump = True
            jump(idx+3)
            veryBigJump = False
    return

jump(0)
print(D[n-1])

##################################################
# import sys

# input = sys.stdin.readline

# N = int(input())
# stones = list(tuple(map(int, input().split())) for _ in range(N - 1))
# stones = [0] + stones
# K = int(input())

# arr = []


# def dfs(idx, use_bigbig_jump, energy_sum):
#     if idx == N:  # 최종 돌까지 갔을 때 든 에너지 총합을 arr에 저장 후 리턴
#         arr.append(energy_sum)
#         return
#     elif idx > N:  # 최종 돌을 넘어가면 리턴
#         return
#     if use_bigbig_jump == False:  # 매우 큰 점프 안했는지 체크한 후, 매우 큰 점프 사용
#         dfs(idx + 3, True, energy_sum + K)

#     dfs(idx + 1, use_bigbig_jump, energy_sum + stones[idx][0])  # 작은 점프
#     dfs(idx + 2, use_bigbig_jump, energy_sum + stones[idx][1])  # 큰 점프


# dfs(1, False, 0)  # 몇번째 돌에 있는지, 매우 큰 점프를 했는지 안했는지, 그 돌까지 갈 때 에너지가 얼마나 들었는지
# print(min(arr))  # N까지 최소 에너지 써서 가는 경우를 출력

##########################################################

# dp = [[200000, 200000] for _ in range(24)]
# dp[0][1] = 0
# n = int(input())
# energys = []
# for _ in range(n - 1):
#     s, b = input().split()
#     energys.append((int(s), int(b)))
# k = int(input())
# for i in range(n-1):
#     for very_big in range(2):
#         dp[i + 1][very_big] = min(dp[i + 1][very_big], dp[i][very_big] + energys[i][0])
#         dp[i + 2][very_big] = min(dp[i + 2][very_big], dp[i][very_big] + energys[i][1])
#     dp[i + 3][0] = min(dp[i + 3][0], dp[i][1] + k)
# print(min(dp[n-1][1], dp[n-1][0]))
