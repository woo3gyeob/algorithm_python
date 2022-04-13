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

    T = int(input())
    for _ in range(T):
        n = int(input())
        stuNums = [0] + list(map(int, input().split()))
        
        visit = [0 for _ in range(n + 1)]
        for stuNum in range(1, n + 1):
            if not visit[stuNum]:
                local_visit = [0 for _ in range(n + 1)]
                dfs(stuNum, [stuNums[stuNum]], 0)

        answer = n - sum(visit)
        print(visit, answer)

if __name__ == '__main__':
    main()