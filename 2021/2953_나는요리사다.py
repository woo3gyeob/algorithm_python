max_score = sum(list(map(int, input().split())))
participant = 1
for i in range(2, 6):
    score = sum(list(map(int, input().split())))
    if max_score < score:
        max_score = score
        participant = i
print('%d %d' %(participant, max_score))