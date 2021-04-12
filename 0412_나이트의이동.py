# 백준 7562 나이트의 이동
# 29828KB, 2876ms
def bfs(r,c):
    S = [(r,c)]
    while S:
        r, c = S.pop(0)
        for i in range(8):
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if nr > -1 and nr < n and nc > -1 and nc < n:
                if not visited[nr][nc]:
                    if nr == er and nc == ec:
                        return visited[r][c]
                    visited[nr][nc] = visited[r][c] + 1
                    S.append((nr,nc))

delta = [(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]

for tc in range(int(input())):
    n = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    visited = [[0]*n for _ in range(n)]
    if sr == er and sc == ec:
        print(0)
    else:
        visited[sr][sc] = 1
        print(bfs(sr,sc))