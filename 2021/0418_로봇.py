# 백준 1726 로봇
# 29028KB, 120ms

def bfs(point):
    S = [point]
    while S:
        p = S.pop(0)
        r, c, d = p[0], p[1], p[2]
        for i in range(4):
            nd = i
            d_turns = direction_turn[d][nd]
            for j in range(1,4):
                nr = r + dr[i]*j
                nc = c + dc[i]*j
                if nr == er and nc == ec:
                    new = visited[r][c][d] + 1 + d_turns + direction_turn[nd][ed]
                    visited[nr][nc][i] = min(new, visited[nr][nc][i])
                    break
                elif nr > -1 and nr < n and nc > -1 and nc < m:
                    if not arr[nr][nc] and visited[nr][nc][i] == 999:
                        visited[nr][nc][i] = visited[r][c][d] + 1 + d_turns
                        S.append((nr,nc,nd))
                    elif not arr[nr][nc] and visited[nr][nc][i] != 999:
                        new = visited[r][c][d] + 1 + d_turns
                        visited[nr][nc][i] = min(new, visited[nr][nc][i])
                    else:
                        break

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())
sr, sc, sd = sr-1, sc-1, sd-1
er, ec, ed = er-1, ec-1, ed-1
direction_turn = [[0,2,1,1],
                  [2,0,1,1],
                  [1,1,0,2],
                  [1,1,2,0]]
# 동서남북
dr = [0,0,1,-1]
dc = [1,-1,0,0]
visited = [[[999]*4 for _ in range(m)] for _ in range(n)]
for i in range(4):
    visited[sr][sc][i] = 0
    
if sr == er and sc == ec:
    print(direction_turn[sd][ed])
else:
    bfs((sr, sc, sd))
    print(min(visited[er][ec]))
