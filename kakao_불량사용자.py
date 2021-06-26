def solution(user_id, banned_id):
    answer = 0
    
    n, m = len(user_id), len(banned_id)
    sel = [0]*m
    visited = [0]*n
    arr = set()
    def perm(idx):
        nonlocal answer
        if idx == m:
            for i in range(m):
                user, ban = sel[i], banned_id[i]
                if len(user) != len(ban): return
                for j in range(len(user)):
                    if ban[j] == '*': continue
                    if user[j] != ban[j]: return
                    
            new = sorted(sel)
            # print(new)
            string = ''.join(new)
            arr.add(string)
            answer += 1
            return
        
        for i in range(n):
            if visited[i]: continue
            visited[i] = 1
            sel[idx] = user_id[i]
            perm(idx+1)
            visited[i] = 0
    
    perm(0)
    # return answer
    return len(arr)


# dic = {1:1, 2:2, 3:3}

# a = sum(dic.values())
# banned_cnt = {}
# n = '****11'
# m = '111111'
# for i in range(len(n)):
#     if n[i] == '*': continue
#     if n[i] != m[i]: break
# else:
#     banned_cnt[n] = banned_cnt.get(n , 0) + 1
# print(banned_cnt)



###########################################
# def solution(user_id, banned_id):
#     answer = 1
#     check = {}
#     for user in user_id:
#         check[user] = 0
    
#     banned_cnt = {}
#     for user in user_id:
#         if check[user]: continue
#         for ban in banned_id:
#             if len(user) != len(ban): continue
            
#             # 문자마다 비교?
#             for i in range(len(user)):
#                 if ban[i] == '*': continue
#                 if user[i] != ban[i]: break
                    
#             else:
#                 banned_cnt[ban] = banned_cnt.get(ban , 0) + 1
                
#     for v in banned_cnt.values():
#         answer *= v
#     print(banned_cnt)
#     return answer

# def solution(user_id, banned_id):
#     answer = 0
    
#     n, m = len(user_id), len(banned_id)
#     sel = [0]*m
    
#     def perm(idx, start):
#         nonlocal answer
#         if idx == m:
#             visit = [0]*m
#             check = [0]*m
#             cnt = 0
#             for i in range(m):
#                 if visit[i]: continue
#                 user = sel[i]
#                 flag = False
#                 for j in range(m):
#                     if check[j]: continue
#                     ban = banned_id[j]
#                     if len(user) != len(ban): continue
#                     for k in range(len(ban)):
#                         if ban[k] == '*': continue
#                         if ban[k] != user[k]: 
#                             print('break:', *sel)
#                             break
#                     else:
#                         flag = True
#                         cnt += 1
#                         visit[i] = 1
#                         check[j] = 1
#                     if flag:
#                         break
#             if cnt == m:
#                 print(sel)
#                 answer += 1
#             return
        
#         for i in range(start, n):
#             sel[idx] = user_id[i]
#             perm(idx+1, i+1)
    
#     perm(0, 0)
    
#     return answer

# arr = [[1,2,3],[2,3,1],[3,2,1]]
# for ar in arr:
#     ar.sort()
# print(arr)