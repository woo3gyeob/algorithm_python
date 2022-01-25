def solution(record):
    answer = []
    dic = {}
    for rec in record:
        if rec[0] == 'E' or rec[0] == 'C':
            flag, uid, name = rec.split(' ')
            dic[uid] = name
    for rec in record:
        if rec[0] == 'E' or rec[0] == 'C':
            flag, uid, _ = rec.split(' ')
        else:
            flag, uid = rec.split(' ')
        name = dic[uid]
        if flag == "Enter":
            message = name + "님이 " + "들어왔습니다."
            answer.append(message)
        elif flag == "Leave":
            message = name + "님이 " + "나갔습니다."
            answer.append(message)
        else:
            continue
    return answer

r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(r))