def solution(record):
    answer = []
    name = {}
    for msg in record:
        cmds = msg.split(" ")
        if cmds[0] == "Enter":
            name[cmds[1]] = cmds[2]
            answer.append([cmds[1], "님이 들어왔습니다."])
        elif cmds[0] == "Leave":
            answer.append([cmds[1], "님이 나갔습니다."])
        else:
            cmds[0] == "Change"
            name[cmds[1]] = cmds[2]
    
    for i in range(len(answer)):
        answer[i] = name[answer[i][0]] + answer[i][1]

    return answer

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
