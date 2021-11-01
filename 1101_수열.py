# 백준 2559 수열
# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# max_val = 0
# total_sum = sum(arr)
# if k < n//2:
#     for i in range(n-k):
#         sum_val = 0
#         for j in range(i, i+k):
#             sum_val += arr[j]
#         if max_val < sum_val:
#             max_val = sum_val

# else:
#     k = n - k
#     for i in range(n-k):
#         sum_val = 0
#         for j in range(i, i+k):
#             sum_val += arr[j]
#         sum_val = total_sum - sum_val
#         if max_val < sum_val:
#             max_val = sum_val

# print(max_val)

#################################
import sys
def solve(n,k,t):
    temp = sum(t[:k])
    ans = temp
    for i in range(k,n):
        temp += t[i]
        temp -= t[i-k]
        if temp > ans:
            ans = temp
    return ans if n != k else temp
if __name__ == "__main__":
    n, k = map(int,sys.stdin.readline().split())
    t = list(map(int,sys.stdin.readline().split()))
    print(solve(n,k,t))