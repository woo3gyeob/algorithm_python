import sys; sys.stdin = open('input (5).txt', 'r')
for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    visit = list(map(int, input().split()))
    visit = sorted(visit) + [0]
    bread = order = 0
    answer = 'Possible'
    for i in range(1, max(visit) + 1):
        if not i % m:
            bread += k
        while visit[order] == i:
            bread -= 1
            order += 1
        if bread < 0:
            answer = 'Impossible'
            break
    print('#%d %s' %(tc, answer))