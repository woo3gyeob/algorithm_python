# 그룹단어체커
n = int(input())
is_groupword = 0
for _ in range(n):
    word = input()
    letter = ''
    if len(word) <= 1:
        is_groupword += 1 # 한글자일때
    else: # 나머지
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                letter += word[i-1]
            if i == (len(word)-1):
                letter += word[i]
        if len(letter) == len(set(word)):
            is_groupword += 1
print(is_groupword)
# aaabbccca set = abc, letter = abca