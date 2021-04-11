N = int(input())
switch = [-1] + list(map(int, input().split())) + [-2] # 앞, 뒤 패딩 추가. 자료 인덱스 범위 (0 ~ n-1) -> (1 ~ n)
n = int(input())
for _ in range(n):
    gender, num = map(int, input().split())
    if gender == 1:             # 남자인 경우
        for i in range(num, N+1, num): # 인덱스가 num의 배수인 것만 스위치 바꿈
            switch[i] = 1 if switch[i] == 0 else 0
    else:                       # 여자인 경우
        switch[num] = 1 if switch[num] == 0 else 0
        for i in range(1, min(num, N - num)+1): # 앞, 뒤 남은 구간 중 최소구간 만큼만 조회[1,0,1,0,1,0,1]
            if switch[num-i] != switch[num+i]:  # 인덱스 num 기준 양쪽 스위치 비교
                break
            switch[num-i] = 1 if switch[num-i] == 0 else 0
            switch[num+i] = 1 if switch[num+i] == 0 else 0

# 한 줄에 20개씩만 출력하기 위한 코드
i, k = 0, N * 1
while k > 0:
    if k >= 20:
        print(' '.join(list(map(str, switch[20*i+1:20*(i+1)+1]))))
    else:
        print(' '.join(list(map(str, switch[20*i+1:N+1]))))
    i += 1
    k -= 20
