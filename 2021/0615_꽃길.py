# 29200 KB/ 172 ms
def perm(idx, start):
    global min_price
    if idx == 3:
        price = 0
        for i in range(3):
            r, c = sel[i]
            price += arr[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                price += arr[nr][nc]
                if price >= min_price:
                    return
        min_price = price
        return

    for i in range(start, nums_length):
        r, c = nums[i] // n, nums[i] % n
        # 가장자리에 있는 좌표는 건너뜀
        if r == 0 or r == n-1 or c == 0 or c == n-1: continue

        # 두 점간 행, 열의 차이의 합이 최소 3이 넘어야 꽃 심을 수 있음
        to_continue = False
        for p in range(idx-1, -1, -1):
            y, x = sel[p]
            if abs(r - y) + abs(c - x) < 3:
                to_continue = True
                break
        if to_continue: continue

        sel[idx] = (r, c)
        perm(idx+1, i+1)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sel = [0]*3
nums = list(range(n+1, n*(n-1)-1))
nums_length = len(nums)

dr = [0,1,0,-1]
dc = [1,0,-1,0]

min_price = 0xffffff
perm(0,0)
print(min_price)


'''
(4,4)에 꽃을 심은 후:1, 꽃을 심을 수 있는 다른 가능한 자리:2는
7
0 0 0 0 0 0 0
0 2 2 0 2 2 0
0 2 0 0 0 2 0
0 0 0 1 0 0 0
0 2 0 0 0 2 0
0 2 2 0 2 2 0
0 0 0 0 0 0 0
'''