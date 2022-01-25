def calc_case(num): # num C 2 구하는 함수
    def f(n):
        a = 1
        for i in range(1, n+1):
            a *= i
        return a
    answer = f(num) // (f(num-2) * f(2))
    return answer
    
N = int(input())
nums = sorted(list(map(int, input().split())))
n = int(input())
answer = 0

for i in range(len(nums)-1):
    if nums[i] <= n and nums[i+1] >= n:
        l, h = nums[i], nums[i+1]
        answer = calc_case(h-l-1) - calc_case(n-l-1) - calc_case(h-n-1)
        break
print(answer)

'''
답 : l ~ h 사이의 모든 구간의 경우의 수 - n을 포함하지 않는 구간의 경우의 수?
예)
l    h
3    11
 n=6

(4 5 6 7 8 9 10 모든 2개의 조합) - (4 5 모든 2개의 조합) - (7 8 9 10 모든 2개의 조합)

그럼 (11-3-1)C2 - (6-3-1)C2 - (11-6-1)C2
'''
