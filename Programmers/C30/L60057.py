def solution(s):
    answer = 1000
    for n in range(1, len(s) + 1):
        tmp = [s[i: i + n] for i in range(0, len(s), n)]
        res = ""
        count = 1
        for x in range(len(tmp)):
            if x < len(tmp) - 1 and tmp[x] == tmp[x + 1]:
                count += 1
            else:
                if count > 1:
                    res += str(count)
                res += tmp[x]
                count = 1
        
        if answer > len(res):
            answer = len(res)

    return answer

if __name__ == "__main__":
    print(solution("xababcdcdababcdcd"))