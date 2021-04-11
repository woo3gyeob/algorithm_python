t = int(input())
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

for _ in range(t):
    m, n = map(int, input().split())
    answer = factorial(n) // (factorial(n-m) * factorial(m))
    print(answer)