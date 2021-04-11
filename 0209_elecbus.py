T = int(input())
answer = []
for test_n in range(1, T+1):
    k, n, m = map(int, input().split())
    station = [0] + list(map(int, input().split())) + [n]
    charge_cnt = 0
    energy = k
    for i in range(1, len(station)-1):
        if (station[i] - station[i-1]) > k:
            answer.append('#'+str(test_n)+' '+str(0)+'\n')
            break
        else:
            energy -= (station[i] - station[i-1])
            if energy < (station[i+1] - station[i]):
                energy = k
                charge_cnt += 1
    else:
        answer.append('#'+str(test_n)+' '+str(charge_cnt)+'\n')
print(''.join(answer))

'''
n = 10
k = 3
0 1 3 5 7 9 10

'''