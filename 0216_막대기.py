x = int(input())
cnt = 1
while x != 1:
    cnt += x % 2
    x //= 2
print(cnt)

