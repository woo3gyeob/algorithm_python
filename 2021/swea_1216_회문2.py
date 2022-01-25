answer = []
for _ in range(10):
    tc = int(input())
    arr = []
    max_len = 1
    for _ in range(100):
        string = input()
        flag = False
        for m in range(99, 0, -1):
            if flag:
                break
            else:
                for i in range(100 - m + 1): # 'abcddcba'
                    for j in range(i, i + m//2):
                        if string[j] != string[i + m - (j - i + 1)]:
                            break
                    else:
                        if m > max_len:
                            max_len = m
                        flag = True
        arr.append(string)
    for col in range(100):
        flag = False
        for m in range(99, 0, -1):
            if flag:
                break
            else:
                for i in range(100 - m + 1):
                    for j in range(i, i + m//2):
                        if arr[j][col] != arr[i + m - (j - i + 1)][col]:
                            break
                    else:
                        if m > max_len:
                            max_len = m
                        flag = True
    answer.append('#%d %d\n' %(tc, max_len))
print(''.join(answer))

'''
col = 2
'abcde'
'bdffs'
'dsged'
...
'''
