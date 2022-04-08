def pow2(n):
    global memo_pow2
    if memo_pow2[n]:
        return memo_pow2[n]
    if n == 0:
        memo_pow2[n] = 1
        return memo_pow2[n]

    tmp_pow2 = pow2(n//2)
    if n % 2:
        memo_pow2[n] = tmp_pow2 * tmp_pow2 * 2
    else:
        memo_pow2[n] = tmp_pow2 * tmp_pow2
    return memo_pow2[n]

def find_combination(n):
    global memo_combi

    if memo_combi[n]:
        return memo_combi[n]
    elif n:
        memo_combi[n] = (pow2(n) - n - 1)
        return memo_combi[n]
    return 0


def main():
    global memo_pow2, memo_combi
    N = int(input())
    string = input().rstrip()
    # memo_pow2 => 2의 거듭제곱 저장
    memo_pow2 = [0 for _ in range(N + 1)]
    memo_combi = [0 for _ in range(N + 1)]

    # memo[N] = [0, 0, 0] => 각각 현재위치에서 나온 w,h,e 개수
    memo = [[0 for _ in range(3)] for _ in range(N + 1)]
    for i in range(N):
        memo[i + 1][0] = memo[i][0]
        memo[i + 1][1] = memo[i][1]
        memo[i + 1][2] = memo[i][2]
        if string[i] == 'W':
            memo[i+1][0] += 1
        elif string[i] == 'H':
            memo[i+1][1] += 1
        elif string[i] == 'E':
            memo[i+1][2] += 1

    answer = 0
    for i in range(N):
        if string[i] != 'H':
            continue
        comb = find_combination(memo[N][2] - memo[i+1][2])
        answer += memo[i+1][0] * comb
        answer %= 1000000007
    print(answer)


if __name__ == "__main__":
    main()
