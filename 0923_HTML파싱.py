# 백준 22859 HTML 파싱
# 31440KB, 280ms

string = input()
divs = string.split('<div title="')
for i in range(1, len(divs)):
    div = divs[i]
    p_list = div.split('<p>')
    title = p_list.pop(0)
    title = title[:-2]
    print('title :', title)
    for ps in p_list:
        sentence = ''
        j = 0
        while j < len(ps):
            if ps[j] == '<':
                for k in range(j+1, len(ps)):
                    if ps[k] == '>':
                        j = k
                        break
            else:
                sentence += ps[j]
            j += 1
        result = sentence.split()
        result = ' '.join(result)
        print(result)


