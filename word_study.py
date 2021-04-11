word = input().upper() # 입력 받은 단어 대문자로
word_dic = {}
max_cnt = 0
for i in set(word):     # MISSISSIPI => MISP 만 조회
    cnt = word.count(i) # MISSISSIPI에 몇 개 들어있는지
    if cnt > max_cnt:   
        max_cnt = cnt
        letter = i
    word_dic[i] = cnt

# ex) word_dic{'A' : 2, 'B': 3. 'E' : 3}  =>  values() = [2,3,3]  =>  max값 3이 2개 있으므로 ? 출력
if list(word_dic.values()).count(max_cnt) > 1:
    print('?')
else:
    print(letter)