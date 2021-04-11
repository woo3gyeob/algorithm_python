# 백준 2660 회장뽑기
# python3 100ms/32756KB, pypy3 156ms/125260KB
from collections import deque

def bfs(idx):
    global score, min_score
    S = deque()
    S.append(idx)
    while S:
        if sum(visited) == n:       # 모든 회원과의 친구관계가 밝혀짐 
            if score < min_score:   # 회장 선출을 위한 최소 점수 갱신
                min_score = score
            break
        score += 1
        for _ in range(len(S)):
            member = S.popleft()
            for i in G[member]:     # member의 친구인 회원들만 조회 
                if not visited[i]:
                    visited[i] = 1
                    S.append(i)


n = int(input())
G = [[] for _ in range(n+1)]    # 모든 회원의 친구목록 저장용 이중리스트
min_score = 987654321
score_list = []                 # 각 회원별 점수 저장 리스트

while True:                     # G에 모든 회원의 친구 번호 저장
    u, v = map(int, input().split())
    if u == -1:
        break
    G[u].append(v)
    G[v].append(u)

for i in range(1,n+1):      # 모든 회원의 점수 계산
    visited = [0]*(n+1)     # 각 회원의 점수 계산을 위한 visited 초기화
    score = 0
    visited[i] = 1
    bfs(i)
    score_list.append(score)
    
boss_candidates = []        # 회장 후보들 저장용 리스트
for i in range(n):
    if score_list[i] == min_score:      # 최소 점수는 bfs 함수 내에서 계속 갱신됨(중복값을 가지는 회원 한 번에 계산때리려고)
        boss_candidates.append(i+1)
print('%d %d' %(min_score, len(boss_candidates)))
print(*boss_candidates)



'''
각 회원별 친구 리스트(G)

0은 빈칸       [[], 
1번사람 친구 : [2], 
2번 "     "  : [1, 3, 4], 
3번 "     "  : [2, 4, 5], 
4번 "     "  : [3, 5, 2], 
5번 "     "  : [4, 3]]
'''