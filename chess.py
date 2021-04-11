# 8 x 8 배열 탐색 함수 (사실 배열은 아니고 8개의 문자열로 이루어진 리스트)
def cnt_BW(arr):
    cnt_W, cnt_B = 0, 0
    for i in range(8):
        for j in range(8):
            if not (i+j)%2: # 행, 열 인덱스의 합이 짝수, 홀수냐에 따라 칠하는 색이 달라진다 (0,0) : 0+0=짝수 : B, (1,0) : 1+0=홀수 : W
                if arr[i][j] != 'W':
                    cnt += 1
            else:
                if arr[i][j] != 'B':
                    cnt += 1
    
        for i in range(8):
            for j in range(8):
                if not (i+j)%2: 
                    if arr[i][j] != 'B':
                        cnt += 1
                else:
                    if arr[i][j] != 'W':
                        cnt += 1
    return min(cnt_W, cnt_B)
# 입력 다 받아서 하나의 리스트로(totlal_arr) 만들기
n, m = map(int, input().split())
total_arr = []
for _ in range(n):
    tmp = input()
    total_arr.append(tmp)
# m*n 배열 total_arr 내에서 가능한 8x8 배열 전부 탐색
min_repair = 8**2
for i in range(n-7):        # 만약 n이 10이면 가능한 연속된 8개의 조합은 10 - 8 + 1 이니까 그 만큼만 조회하면 됨
    for j in range(m-7):
        test_arr = list(map(lambda x : x[j:j+8], total_arr[i:i+8])) # 8x8 행렬이 만들어짐
        cnt = cnt_BW(test_arr)
        if cnt < min_repair:
            min_repair = cnt
print(min_repair)

# 3 x 5 배열-> 3 x 3 lambda ; a[1:4]
'''
['aaaaa',
 'bbbbb',
 'ccccc']
 '''