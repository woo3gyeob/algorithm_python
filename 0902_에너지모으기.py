# 백준 16198 에너지 모으기
# https://www.acmicpc.net/problem/16198
# 30476KB, 136ms

n = int(input())
arr = list(map(int, input().split()))
energyList = []
def dfs(n, arr, energy):
    if n == 2:
        energyList.append(energy)
        return
    for i in range(1, n-1):
        new_energy = arr[i-1] * arr[i+1]
        dfs(n-1, arr[:i] + arr[i+1:], energy + new_energy)

dfs(n, arr, 0)
print(max(energyList))