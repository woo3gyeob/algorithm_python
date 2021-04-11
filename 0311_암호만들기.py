def perm(idx, start):
    if idx == m:
        vowel_cnt = 0
        for i in sel:
            if i in vowel:
                vowel_cnt += 1
        if vowel_cnt >= 1 and (m - vowel_cnt) >= 2:
            print(''.join(sel))
        return
    for i in range(start, n):
        if not checked[i]:
            sel[idx] = letters[i]
            checked[i] = 1
            perm(idx+1, i+1)
            checked[i] = 0

m, n = map(int, input().split())
letters = input().split()
vowel = 'aeiou'
letters = sorted(letters, key = lambda x : ord(x)) # 'a' 'e' 'c' -> ord('a') a c e
checked = [0]*n
sel = [0]*m
perm(0,0)