# https://www.acmicpc.net/problem/1474
# 백준 1474 밑 줄
# ~ 91 : 대문자
# 30864KB, 72ms

n, m = map(int, input().split())
words = []
total_length = 0

for _ in range(n):
    word = input()
    words.append(word)
    total_length += len(word)

essential_underline_length, remained_length = (m - total_length) // (n - 1), (m - total_length) % (n - 1)

additional_underline_word_array = [0] * n

for i in range(1, n):
    if remained_length == 0:
        break
    first_letter = words[i][0]
    # print(1, first_letter, ord(first_letter))
    if ord(first_letter) > 91:
        additional_underline_word_array[i] = 1
        remained_length -= 1
    
for i in range(n-1, 0, -1):
    if remained_length == 0:
        break
    first_letter = words[i][0]
    # print(2, first_letter, ord(first_letter))
    if ord(first_letter) < 93:
        additional_underline_word_array[i] = 1
        remained_length -= 1

answer = words[0]
for i in range(1, n):
    if additional_underline_word_array[i]:
        answer += "_" * (essential_underline_length + 1) + words[i]

    else:
        answer += "_" * essential_underline_length + words[i]

# print(additional_underline_word_array)
print(answer)
# print(ord('s'))

########################################################
# 52ms 답변
s=input;n,m=map(int,s().split());l=[];h=0;a=[]
exec('t=s();a+=[t[0].isupper()];h+=len(t);l+=[t];'*n)
s=(m-h)%(n-1);r=''
for i in range(n):
 if i!=0and s>0and(n-i<=s or a[i]<1):r+='_';s-=1
 r+=l[i]+(m-h)//(n-1)*'_'
print(r[:m])