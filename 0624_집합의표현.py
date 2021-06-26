# import sys
# sys.setrecursionlimit(10**7)

# n, m = map(int, input().split())
# parent = [i for i in range(n+1)]

# def is_contain(t):
#     if t != parent[t]:
#         parent[t] = is_contain(parent[t])
#     return parent[t]

# def union(a, b):
#     a_ = is_contain(a)
#     b_ = is_contain(b)
    
#     if a_ < b_ :
#         parent[b_] = a_
#     else:
#         parent[a_] = b_

# for i in range(m):
#     flag, a, b = map(int, input().split())
#     if flag == 0:
#         union(a, b)
#     else:
#         if is_contain(a) == is_contain(b):
#             print('YES')
#         else:
#             print('NO')

#########################################################

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(a, b)
    elif opr == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
