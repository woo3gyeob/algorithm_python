from decimal import *
def normalization(x, y):
    return x/(x**2 + y**2)**0.5, y/(x**2 + y**2)**0.5

def get_distance(ax, ay, bx, by):
    return ((bx - ax)**2 + (by - ay)**2)**0.5

getcontext().prec = 16

ax, ay, bx, by, cx, cy = map(int, input().split())
ab_x, ab_y = bx - ax, by - ay       # a->b 벡터
ac_x, ac_y = cx - ax, cy - ay       # a->c 벡터
bc_x, bc_y = cx - bx, cy - by       # b->c 벡터

abx, aby = normalization(ab_x, ab_y) # 정규화
acx, acy = normalization(ac_x, ac_y)
bcx, bcy = normalization(bc_x, bc_y)

dot1 = abx * bcx + aby * bcy # 내적 -1 ~ 1 (평행하면 1, 평행인데 반대방향이면 -1)
dot2 = abx * acx + aby * acy
dot3 = bcx * acx + bcy * acy

if abs(dot1) == abs(dot2) == abs(dot3):
    print(-1.0)
else:
    ab = get_distance(ax, ay, bx, by) # 주어진 세 점을 잇는 각 변의 길이를 구한다
    ac = get_distance(ax, ay, cx, cy)
    bc = get_distance(bx, by, cx, cy)
    ls = [ab, ac, bc]
    ls.sort()
    print((ls[2] - ls[0]) * decimal.Decimal(2)) # 가장 긴 둘레 - 가장 짧은 둘레 = 2 x (가장 긴 변 - 가장 짧은 변)