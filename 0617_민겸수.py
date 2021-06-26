
string = input()
n = len(string)
min_num = ''
max_num = ''
tmp = 0     # M개수 세는용
for i in range(n):
    if string[i] == 'K':
        if tmp > 0:
            min_num += str(10**(tmp-1))
        min_num += '5'
        max_num += str(5 * (10 ** tmp))
        tmp = 0
    else:
        tmp += 1
    if i == n-1 and string[i] == 'M':
        min_num += str(10**(tmp-1))
        max_num += '1'*tmp

print(max_num)
print(min_num)

# M K K M M K