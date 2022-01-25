n = int(input())
ls = []
for _ in range(n):
    score = int(input())
    ls.append(score)
cnt = 0
for i in range(n-2,-1,-1):
    if ls[i] >= ls[i+1]:
        cnt += ls[i] - ls[i+1] + 1
        ls[i] -= (ls[i] - ls[i+1] + 1)
print(cnt)