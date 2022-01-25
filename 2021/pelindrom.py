def pelindrom(num):
    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            return 'no'
    return 'yes'

while True:
    num = input()
    if num == '0':
        break
    print(pelindrom(num))

'''
number :  1 2 3 4 5 4 3 2 1
---------------------------
index  :  0 1 2 3 4 5 6 7 8

----------------------------------------- start

number[0] == number[8]
number[1] == number[7]
number[2] == number[6]
number[3] == number[5]
----------------------------------------- enough
number[4] : mid
number[5] == number[3]
number[6] == number[2]
number[7] == number[1]
number[8] == number[0]
---------------------------------------- not necessary