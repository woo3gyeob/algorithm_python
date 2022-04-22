import re

def solution(new_id):
    answer = new_id + ''
    answer1 = answer.lower()
    answer2 = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', answer1)
    # answer3 = re.sub('(([.])\\2{1,}', '', answer2)
    answer3 = re.sub('[.]+', '.', answer2)
    if answer3[0] == '.':
        answer3 = answer3[1:]
    # print(answer3)
    if answer3:
        if answer3[-1] == '.':
            answer3 = answer3[:-1]
    # print(answer3)
    if not answer3:
        answer3 = 'a'
    # print(answer3)
    if len(answer3) > 15:
        answer3 = answer3[:15]
    # print(answer3)
    if answer3[-1] == '.':
        answer3 = answer3[:-1]
    # print(answer3)
    if len(answer3) < 3:
        add_letter = answer3[-1] * (3 - len(answer3))
        answer3 = answer3 + add_letter
    # print(answer3)
    # print(answer7)
    return answer3

# solution("...!@BaT#*..y.abcde-_fg-_hijklm")
print(solution("=.="))

####################################################################
### 맞는 풀이 ###
import re

def solution(new_id):
    answer = ''
    # 1단계 & 2단계 : 소문자 치환
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    # 3단계 : 마침표 2번 이상 > 하나로
    answer = re.sub('\.\.+', '.', answer)
    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)
    # 5단계 : 빈 문자열이면 a 대입
    if answer == '':
        answer = 'a'
    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])
    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1:]
    return answer