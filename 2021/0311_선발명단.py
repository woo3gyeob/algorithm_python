def perm(position):
    global max_val
    if position == 11:
        if max_val < sum(sel):
            max_val = sum(sel)
        return
    for player in candidates[position]:
        if not checked[player]:
            sel[position] = arr[player][position]
            checked[player] = 1
            perm(position+1)
            checked[player] = 0

for _ in range(int(input())):
    arr = []
    candidates = [[] for _ in range(11)]
    for player in range(11):
        score = list(map(int, input().split()))
        for i in range(11):
            if score[i] > 0:
                candidates[i].append(player)
        arr.append(score)
        
    checked = [0]*11
    sel = [0]*11
    max_val = 0
    perm(0)
    print(max_val)
