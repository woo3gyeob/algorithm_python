# https://www.acmicpc.net/problem/22868
# 백준 22868 산책 (small)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

S, E = map(int, input().split())

visit = [0] * (n + 1)
visit[S] = 1

answer = 0

# 각 노드의 갈 수 있는 노드들 정렬
for i in range(1, n+1):
    arr[i].sort()

Q = deque()
Q.append((S, visit))

end_signal = False

while Q:
    node, path = Q.popleft()
    # print('for문 밖에 node, path 체크', node, path)
    for new_node in arr[node]:
        if path[new_node]: continue
        path[new_node] = 1
        # print(new_node, '번 노드 방문, 길 : ', path)
        if new_node == E:
            end_signal = True
            break
        Q.append((new_node, path[:]))
        path[new_node] = 0

    if end_signal:
        break

# print(path)
path[S] = 0

answer += sum(path)

Back_Q = deque()
Back_Q.append((E, path))

end_signal = False

while Back_Q:
    node, path = Back_Q.popleft()
    for new_node in arr[node]:
        if path[new_node]: continue
        path[new_node] = 1
        if new_node == S:
            end_signal = True
            answer += sum(path) - 1
            break
        Back_Q.append((new_node, path[:]))
        path[new_node] = 0

    if end_signal:
        break

# print(path)
print(answer)