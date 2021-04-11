# 백준 17471
def perm(num, idx):
    global min_val
    nodes_not_in_sel = [x for x in all_nodes if x not in sel]
    nodes_not_in_sel.sort()
    start = nodes_not_in_sel[0]
    possible_nodes = [start]
    checked[start] = 1
    p_nodes = possible_nodes[:]
    def dfs(node, rest):
        for i in G[node]:
            if not checked[i] and i in rest:
                checked[i] = 1
                p_nodes.append(i)
                dfs(i, rest)
                p_nodes.remove(i)
    
    dfs(start, nodes_not_in_sel)
    print(p_nodes.sort(), nodes_not_in_sel)
    
    if p_nodes.sort() != nodes_not_in_sel:
        print("탈출!!!")
        return
    else:
        sum_val = 0
        for i in nodes_not_in_sel:
            sum_val += arr[i]
        if abs(2 * sum_val - sum_people) < min_val:
            min_val = abs(2 * sum_val - sum_people)
    if idx == n:
        return
    for i in G[idx]:
        if not visited[i]:
            visited[i] = 1
            sel.append(i)
            perm(i, idx+1)
            visited[i] = 0
            sel.remove(i)

def dfs(node, rest):
    for i in G[node]:
        if not checked[i] and i in rest:
            checked[i] = 1
            p_nodes.append(i)
            dfs(i, rest)
            
n = int(input())
arr = [0] + list(map(int, input().split()))
G = [[] for _ in range(n+1)]
num_of_nodes = [0]*(n+1)
for i in range(1, n+1):
    ls = list(map(int, input().split()))
    j = ls.pop(0)
    num_of_nodes[i] = j
    G[i] = ls
all_nodes = list(range(1,n+1))
min_val = 987654321
sum_people = sum(arr)
p_nodes = []
for i in range(1, n+1):
    sel = [i]
    visited = [0]*(n+1)
    checked = [0]*(n+1)
    perm(i, 0)
print(min_val)

# 모든 조합을 뽑는다? - 저장까지? - 초과다
# 모든 조합을 뽑는다 - 뽑을때마다 dfs 돌린다 - 안되네:? 그럼말구,,,