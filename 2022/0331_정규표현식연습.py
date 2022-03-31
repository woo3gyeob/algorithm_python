import re
import string
# ------------------------------------------- re.match ---------------------------------------------------------------
# re.match(찾고 싶은 문자열, 대상 문자열) : 대상 문자열에서 첫 문자열부터 일치하는 패턴을 찾고 싶을 때
string = 'abc123aec'
m1 = re.match('abc', string)
print(m1.group()) # .group을 쓰면 일치하는 문자열 출력 : abc

m2 = re.match('a.c', string)
print(m2.group())

'''
match는 `첫 문자열`이 일치하는 지 보기 때문에 잘 안씀 -> search를 많이 씀
'''

# ------------------------------------------- re.search ---------------------------------------------------------------
# re.search : 아무 곳에서나 일치하는 문자열을 찾고 싶을 때
m3 = re.search('a.c', string)
print(m3.group()) # 출력 : abc (aec는 안나옴 왜?)

'''
하지만 search도 일치하는 걸 하나만! 찾을 수 있음
'''

# ------------------------------------------- re.findall ---------------------------------------------------------------
m4 = re.findall('a.c', string)
print(m4)

m5 = re.findall('[a-zA-Z]+', string)
print(m5)

string2 = 'jongs3030@naver.com 01034556665 jason jongs0206@gmail.com 01033442222 jong'
m6 = re.findall('[\w]+@[\w]+.[\w]+', string2)
print(m6)