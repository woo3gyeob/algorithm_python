def perm(idx):
    global sum_val, max_val
    if sum_val > m: # m보다 크면 불가능한 순열이니까 더 이상 조회할 필요 X
        return
    if idx == 3: # 3개 숫자 합이 m 이하면서
        if sum_val > max_val: # 기존 max값보다 크면 갱신
            max_val = sum_val
            return
    else:
        for i in range(n):
            if not checked[i]:
                checked[i] = 1
                sum_val += ls[i]
                perm(idx + 1)
                checked[i] = 0
                sum_val -= ls[i]

n, m = map(int, input().split())
ls = list(map(int, input().split()))
sum_val = max_val = 0
checked = [0] * n
perm(0)
print(max_val)