N = int(input())

def plus_cycle(n):

    n = (n%10)*10 + (n//10 + n%10)%10
    if n == N:
        return 1
    return 1 + plus_cycle(n)

print(plus_cycle(N))
