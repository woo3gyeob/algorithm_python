w, h = map(int, input().split())
n = int(input())
row, col = [0], [0] # 앞에 0 패딩 추가 
for _ in range(n):
    rc, idx = map(int, input().split())
    if rc == 1:
        row.append(idx)
    else:
        col.append(idx)
row.sort() # 입력되는 수가 차례대로 들어오는게 아니므로 오름차순 정렬 필요
col.sort()
row = row + [w]  # 뒤에 너비 w 패딩 추가 ex) 너비 10, 자르는 번호가 [3, 5, 7]이면 양 끝 패딩 ->  [0, 3, 5, 7, 10]
col = col + [h]  # 뒤에 높이 h 패딩 추가
max_area = 0
for i in range(1, len(row)):
    for j in range(1, len(col)):
        area = (row[i] - row[i-1]) * (col[j] - col[j-1]) # 너비 계산(인덱스 1부터 시작) 3-0, 5-3, 7-5, 10-7
        if area > max_area:
            max_area = area
print(max_area)