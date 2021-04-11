pic = int(input()) # 사진틀 개수
n = int(input())   # 총 추천수
stu = list(map(int, input().split())) # 학생 번호 리스트
rec = [stu[0]]      # 추천할 학생들 번호 넣는 리스트
cnt = [1]           # 추천 횟수 저장하는 리스트
for i in range(1, n):
    if stu[i] in rec:                   # 새로운 추천 번호가 기존에 추천받은 번호에 있을 때
        for j in range(len(rec)):       
            if rec[j] == stu[i]:        # 추천 횟수 1 더해줌
                cnt[j] += 1             
    else:                               # 새로운 추천 번호가 기존에 없는 번호인 경우인데
        if len(rec) >= pic:             # 추천 리스트가 가능한 추천수를 이미 채웠다면
            for j in range(len(rec)):   
                if cnt[j] == min(cnt):  # 추천수가 가장 낮은 놈 제거
                    del rec[j]          # 또 만약에 추천수가 같아도 append로 해주기 때문에 먼저 온 놈이 먼저 제거되게 되있음
                    del cnt[j]
                    break
        rec.append(stu[i])              # 박힌 돌 빼내고 굴러온 돌이 새로 박힘
        cnt.append(1)                   # 새로 왔으니 추천 수 1로 초기화
rec.sort()
print(' '.join(list(map(str, rec))))