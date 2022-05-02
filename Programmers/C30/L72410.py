import re
def solution(new_id):
    answer = ''

    #1
    answer = new_id.lower()
    #2
    answer = re.sub("[^a-z0-9-_.]", "", answer)
    #3
    answer = re.sub("[.]+", ".", answer)
    #4
    answer = re.sub("^[.]+|[.]+$", "", answer)
    #5
    if answer == "":
        answer += "a"
    #6
    if len(answer) > 15:
        answer = answer[:15]
        answer = re.sub("[.]+$", "", answer)
    
    #7
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer

if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))