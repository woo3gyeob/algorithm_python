# https://www.acmicpc.net/problem/9466
# 백준 9466 텀 프로젝트
# 시간초과 

def main():

    def dfs(first_stuNum, stuNum_array, idx):
        nonlocal visit, local_visit
        if first_stuNum == stuNum_array[idx]:
            for stuNum in stuNum_array:
                visit[stuNum] = 1
            return

        new_stuNum = stuNums[stuNum_array[idx]]
        if local_visit[new_stuNum]:
            return
        
        local_visit[new_stuNum] = 1
        return dfs(first_stuNum, stuNum_array + [new_stuNum], idx + 1)


    def bfs(first_stuNum, stuNum_array, idx):
        nonlocal visit, local_visit
        while True:
            if first_stuNum == stuNum_array[idx]:
                for stuNum in stuNum_array:
                    visit[stuNum] = 1
                return
            
            new_stuNum = stuNums[stuNum_array[idx]]
            if local_visit[new_stuNum]:
                return
            
            local_visit[new_stuNum] = 1
            idx += 1
            stuNum_array.append(new_stuNum)


    T = int(input())
    for _ in range(T):
        n = int(input())
        stuNums = [0] + list(map(int, input().split()))
        
        visit = [0 for _ in range(n + 1)]
        for stuNum in range(1, n + 1):
            if not visit[stuNum]:
                local_visit = [0 for _ in range(n + 1)]
                bfs(stuNum, [stuNums[stuNum]], 0)

        answer = n - sum(visit)
        print(answer)

if __name__ == '__main__':
    main()



import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    from_count = [0 for _ in range(n+1)]
    for num in nums:
        from_count[num] += 1

    d = deque()
    for i in range(1, n+1):
        if from_count[i] == 0:
            d.append(i)
            from_count[i] -= 1

    answer = 0
    while d:
        student = d.pop()
        answer += 1
        from_count[nums[student]] -= 1
        if from_count[nums[student]] == 0:
            d.append(nums[student])

    print(answer)