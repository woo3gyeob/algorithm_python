# 백준 2224 명제 증명
# 시간초과
import sys

def dfs(start, s, ls):
    if s not in dic.keys(): return
    for i in dic[s]:
        if i in ls: continue
        arr.add((start, i))
        arr.add((s, i))
        dfs(start, i, ls+[i])

n = int(input())
dic = {}
for _ in range(n):
    p, __, q = sys.stdin.readline().split(' ')
    q = q.split('\n')[0]
    dic[p] = dic.get(p, []) + [q]

# A => b
# b => C
# A => C
# dic = ['A':['b','C], 'b':['C']]

arr = set()
for start in dic.keys():
    dfs(start, start, [start])

arr = list(arr)
arr.sort(key=lambda x: [x[0], x[1]])
m = len(arr)
print(m)
for p, q in arr:
    print(p + ' => ' + q)

'''
정답코드
_INF = 1e9
def solution():
    N = int(input())
    Floyd = [[_INF for _ in range(52)] for _ in range(52)]

    for _ in range(N):
        answer = (input().split(' '))
        dx, dy = 0, 0
        if 'A' <= answer[0] <= 'Z': dx = ord(answer[0]) - 65
        else: dx = ord(answer[0]) - 71
        if 'A' <= answer[2] <= 'Z': dy = ord(answer[2]) - 65
        else: dy = ord(answer[2]) - 71

        Floyd[dx][dy] = 1

    for k in range(52):
        for i in range(52):
            for j in range(52):
                Floyd[i][j] = min(Floyd[i][j], Floyd[i][k] + Floyd[k][j])

    cnt = 0
    for i in range(52):
        for j in range(52):
            if i == j: continue
            if Floyd[i][j] != _INF:
                cnt += 1
    print(cnt)
    for i in range(52):
        for j in range(52):
            ret = ''
            if i == j: continue
            if Floyd[i][j] == _INF:
                continue
            if 0 <= i < 26: ret += chr(i + 65)
            else: ret += chr(i + 71)

            ret += ' => '

            if 0 <= j < 26: ret += chr(j + 65)
            else: ret += chr(j + 71)

            print(ret)

solution()
'''