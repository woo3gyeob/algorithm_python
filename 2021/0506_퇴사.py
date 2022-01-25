# 백준 14501 퇴사
# https://www.acmicpc.net/problem/14501

def perm(day, payoff):
    global max_payoff
    if day >= n:
        if payoff > max_payoff:
            max_payoff = payoff
        return
    if day + reservation[day][0] <= n:
        perm(day + reservation[day][0], payoff + reservation[day][1])
    perm(day+1, payoff)


n = int(input())
reservation = []
for i in range(n):
    m, pay = map(int, input().split())
    reservation.append((m, pay))
max_payoff = 0
perm(0,0)
print(max_payoff)