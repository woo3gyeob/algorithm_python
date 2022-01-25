# 백준 13164 
n, k = map(int, input().split())
arr = list(map(int, input().split()))
min_cost = 0xffffff

def comb(idx, start, cost, cnt):
    global min_cost
    if cost >= min_cost:
        return
    if idx == n-1 or cnt == k-1:
        cost += arr[n-1] - arr[start]
        if cost < min_cost:
            min_cost = cost
        return
    comb(idx+1, idx+1, cost + arr[idx] - arr[start], cnt+1)
    comb(idx+1, start, cost, cnt)

comb(0,0,0,0)
print(min_cost)


## 그리디
# 62820KB, 332ms
n, k = map(int, input().split())
arr = list(map(int, input().split()))
costs = [0]*(n-1)
for i in range(n-1):
    costs[i] = arr[i+1] - arr[i]

costs.sort()
print(sum(costs[:n-k]))