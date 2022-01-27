import sys
from bisect import bisect_right

input = sys.stdin.read


def sol2343():
    n, m, *args = map(int, input().split())
    s, e = max(args), sum(args)
    for i in range(n - 1):
        args[i + 1] += args[i]
    while s <= e:
        mid = (s + e) // 2
        if simulate(args, mid, m):
            e = mid - 1
        else:
            s = mid + 1
    return e + 1


def simulate(args, size, m):
    sub = 0
    for _ in range(m):
        sub = args[bisect_right(args, size + sub) - 1]
        if sub == args[-1]:
            break
    return True if sub == args[-1] else False


if __name__ == '__main__':
    print(sol2343())