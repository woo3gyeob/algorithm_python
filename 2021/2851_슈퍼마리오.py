mushroom, flag, answer = 0, False, None
for i in range(10):
    n = int(input())
    if mushroom + n >= 100 and flag == False:
        a, b = 100 - mushroom, mushroom + n - 100
        answer = mushroom if a < b else mushroom + n
        flag = True
    mushroom += n
print(mushroom if answer is None else answer)