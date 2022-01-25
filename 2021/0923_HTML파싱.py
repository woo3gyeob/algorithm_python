# 백준 22859 HTML 파싱
# 31440KB, 280ms

'''
<main><div title="title_name_1"><p>paragraph 1</p><p>paragraph 2 <i>Italic Tag</i> <br > </p><p>paragraph 3 <b>Bold Tag</b> end.</p></div><div title="title_name_2"><p>paragraph 4</p><p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p></div></main>
'''

string = input()
divs = string.split('<div title="')
for i in range(1, len(divs)):
    div = divs[i]
    p_list = div.split('<p>')
    title = p_list.pop(0)
    title = title[:-2]
    print('title :', title)
    # p태그들
    for ps in p_list:
        sentence = ''
        j = 0
        while j < len(ps):
            # 태그기호는 다 제거 '<' 나오면 '>' 나올 때까지 스킵
            if ps[j] == '<':
                for k in range(j+1, len(ps)):
                    if ps[k] == '>':
                        j = k
                        break
            else:
                sentence += ps[j]
            j += 1
        # 띄어쓰기 한칸씩만 만들어주기
        result = sentence.split()
        result = ' '.join(result)
        print(result)


