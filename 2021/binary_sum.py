# 이진수 합 (십진수 변환 후 덧셈)
a, b = input().split()
a_dec = 0 # 첫 번째 입력값의 십진수를 저장할 변수
b_dec = 0 # 두 번째 입력값의 십진수를 저장할 변수
# 두 십진수 계산
for i in range(len(a)):
    a_dec += int(a[-(i+1)]) * (2**i)
for j in range(len(b)):
    b_dec += int(b[-(j+1)]) * (2**j)

'''
(1011)2  = 1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1* 2^3 = 11
'''
answer = '' # 두 수의 합의 이진수를 저장할 변수
num = a_dec + b_dec # 두 십진수의 합

# 두 수의 합의 이진수 계산
while True:
    if num <= 1:
        answer = str(num)
        break
    if num <= 3:
        answer = str(1) + str(num%2) + answer
        break
    answer = str(num%2) + answer
    num = num//2
print(answer)

'''
2로 나눈 몫이 2 또는 3이 되면, 앞에 '1'과 2로 나눈 나머지를 이어 붙이면 된다.
몫 수   나머지
2  10  -- 0
2  5   -- 1
2  2   -- 0
   1

몫 수   나머지
2  7   -- 1
2  3   -- 1
   1
'''