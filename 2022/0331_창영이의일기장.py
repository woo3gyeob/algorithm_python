# https://www.acmicpc.net/problem/2954
# 백준 2954 창영이의 일기장

import re

diary = input()
m = re.findall('([a-zA-Z]+)([a|e|i|o|u]p[a|e|i|o|u])', diary)
print(m)