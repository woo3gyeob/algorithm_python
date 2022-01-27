# https://www.acmicpc.net/problem/2343
# 백준 2343 기타 레슨
# 시간초과
n, m = map(int, input().split())
arr = list(map(int, input().split()))

sel = [0] * m
sel.append(n-1)
min_blueray = 0xfffffff

def perm(idx, start):
    global min_blueray
    if idx == m:
        blueray_size_array = []
        for i in range(1, m+1):
            new_blueray = sum(arr[sel[i-1]+1:sel[i]+1])
            if new_blueray >= min_blueray:
                return
            blueray_size_array.append(new_blueray)
        # print(sel, blueray_size_array)
        min_blueray = max(blueray_size_array)
        
        return
    
    for i in range(start, n - m + 1 + idx):
        sel[idx] = i
        perm(idx+1, i+1)


perm(1, 0)
print(min_blueray)


########### 500ms 코드 ############
# 이분 탐색
def add_lesson():
    cnt = 0  # 레코드 갯수 세기
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합
    for i in range(N):
        if sum_lesson + lesson_list[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += lesson_list[i]
    else:
        if sum_lesson:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())  # N: 레슨 수, M: 블루레이 수
    lesson_list = list(map(int, input().split()))  # 레슨들

    right = sum(lesson_list)   # 레슨을 하나의 레코드에 다 담을 수 있을 때 레코드의 크기는 레슨의 합이다
    left = max(lesson_list)  # 레코드가 가질 수 있는 가장 작은 크기
    while left <= right:
        # 레코드 크기 중간값 구하기
        mid = (left + right) // 2
        cnt = add_lesson()
        if cnt <= M:  # 레코드 숫자가 모자라면 레코드 크기(mid)를 줄인다.
            right = mid - 1
        elif cnt > M:  # 레코드 숫자가 더 많아지면 레코드 크기(mid)를 늘린다
            left = mid + 1

    # 답은 left 에 있다. (최소 크기)
    print(left)


################ 최단 시간 코드 from baekjoon ###################

import sys
from bisect import bisect_right

input = sys.stdin.read


def sol2343():
    n, m, *seq = map(int, input().split())
    s, e = max(seq), sum(seq)
    for i in range(n - 1):
        seq[i + 1] += seq[i]
    while s <= e:
        mid = (s + e) // 2
        if simulate(seq, mid, m):
            e = mid - 1
        else:
            s = mid + 1
    return e + 1


def simulate(seq, size, m):
    sub = 0
    for _ in range(m):
        sub = seq[bisect_right(seq, size + sub) - 1]
        if sub == seq[-1]:
            break
    return True if sub == seq[-1] else False


if __name__ == '__main__':
    print(sol2343())
