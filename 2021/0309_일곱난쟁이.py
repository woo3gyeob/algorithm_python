# 9개 중 2개의 조합을 구해 
# 총합 - sum(2개 숫자) = 100 이 나오는 sum의 조합을 하나 찾고 빠지기
def perm(idx):
    if idx == 2:
        if sum(sel) == remain: # 2개 숫자 합이 remain이랑 같다면
            for i in sel:
                height.remove(i) # height에서 두개 숫자 제거
            return 1
        return 0
    if sum(sel) > remain: # remain보다 크면 더 조회할 필요X
        return 0
    for i in range(9):
        if not checked[i]:
            sel[idx] = height[i]
            checked[i] = 1
            if perm(idx + 1): return 1 # 조합 하나라도 찾으면 종료
            sel[idx] = 0
            checked[i] = 0

height = [int(input()) for _ in range(9)]
remain = sum(height) - 100 # 찾아야하는 2개 숫자 합
checked = [0] * 9
sel = [0] * 2
perm(0)
height.sort()
for i in height:
    print(i)