# 이진수 자체로 더하기
a, b = input().split()
#########################################################################################
#### 두 이진수 길이를 비교해 더 짧은 수에 짧은 칸만큼 0을 채우고 두 수를 더한 후 시작 ####
a, b = str(int(a)), str(int(b))

if len(a) > len(b):
    b = '0'*(len(a) - len(b)) + b
else:
    a = '0'*(len(b) - len(a)) + a
ab_sum = [int(b[i]) + int(a[i]) for i in range(len(a))]
#########################################################################################
for i in range(1, len(ab_sum)+1):
    if i == len(ab_sum):        # 마지막 부분 연산
        if ab_sum[-i] > 1:      # 마지막 부분이 1보다 크면 ex) 2 or 3
            ab_sum[-i] = ab_sum[-i] % 2     # 2로 나눈 나머지를 그 자리에 넣어주고
            print('1' + ''.join(list(map(str, ab_sum))))    # 앞에 1을 붙이고 나머지 join으로 합쳐주면 정답
        else:
            print(''.join(list(map(str, ab_sum))))          # 마지막 부분이 1보다 큰게 아니면 그냥 그대로 join해서 출력
        break
    if ab_sum[-i] > 1:          # 
        ab_sum[-(i+1)] += 1
    ab_sum[-i] = ab_sum[-i] % 2


'''
(1011) + (1001) = (2012)
앞부분 부터 시작
2 -> 1보다 큼 -> 다음꺼에 +1하고 해당 자리에 2로 나눈 나머지 할당 -> 2020
2 -> 1보다 큼 -> 다음꺼에 +1, 해당자리 2로 나눈 나머지 -> 2100
1 -> 1보다 크지 않음 -> 그대로 2100
2 -> 1보다 크고 마지막임 -> 앞에 1 붙이고 해당 자리는 2로 나눈 나머지 입력하고 출력 -> 10100
'''

2202
def bin(n)
2 
나머지 1
몫 +1
return 나머지 + bin(다음꺼)