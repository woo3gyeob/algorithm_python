# 백준 15661
# pypy3 136736KB, 1600ms
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
total = list(range(n))
min_diff = 0xffffff
def calc():
    global min_diff
    linkTeam = [i for i in total if i not in startTeam]
    link_ability, start_ability = 0, 0
    l, s = len(linkTeam), len(startTeam)
    if l == 1: link_ability = 0
    else:
        for i in range(l-1):
            for j in range(i+1, l):
                link_ability += arr[linkTeam[i]][linkTeam[j]]
                link_ability += arr[linkTeam[j]][linkTeam[i]]
    if s == 1: start_ability = 0
    else:
        for i in range(s-1):
            for j in range(i+1, s):
                start_ability += arr[startTeam[i]][startTeam[j]]
                start_ability += arr[startTeam[j]][startTeam[i]]
    diff = abs(link_ability - start_ability)
    if diff < min_diff:
        min_diff = diff
    return

def comb(idx, s):
    if idx == target:
        calc()
        return
    for i in range(s, n):
        startTeam[idx] = i
        comb(idx+1, i+1)

for target in range(1, n//2 + 1):
    startTeam = [0]*target
    comb(0,0)

print(min_diff)