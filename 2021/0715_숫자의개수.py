# 백준 2577
a = int(input())
b = int(input())
c = int(input())
val = a*b*c
val = str(val)
for num in range(10):
    print(val.count(str(num)))