# 백준 2224 명제 증명
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


arr = set()
for start in dic.keys():
    dfs(start, start, [start])

arr = list(arr)
arr.sort(key=lambda x: [x[0], x[1]])
m = len(arr)
print(m)
for p, q in arr:
    print(p + ' => ' + q)