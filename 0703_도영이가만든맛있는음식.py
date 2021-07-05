# n = int(input())
# sours = []
# bitters = []
# for _ in range(n):
#     sour, bitter = map(int, input().split())
#     sours.append(sour)
#     bitters.append(bitter)

# def comb(idx, start, s, b):
#     global min_difference
#     if idx == target:
#         if abs(s-b) < min_difference:
#             min_difference = abs(s-b)
#         return

#     for i in range(start, n):
#         comb(idx+1, i+1, s*sours[i], b+bitters[i])

# min_difference = 0xfffffff
# for target in range(1,n+1):
#     comb(0,0,1,0)

# print(min_difference)



n = int(input())
sours = []
bitters = []
for _ in range(n):
    sour, bitter = map(int, input().split())
    sours.append(sour)
    bitters.append(bitter)

def comb(idx, i, s, b):
    global min_difference
    if i >= n: return
    if idx == target:
        if abs(s-b) < min_difference:
            min_difference = abs(s-b)
        return

    comb(idx+1, i+1, s*sours[i], b+bitters[i])
    comb(idx, i+1, s, b)

min_difference = 0xfffffff
for target in range(1,n+1):
    comb(0,0,1,0)

print(min_difference)
