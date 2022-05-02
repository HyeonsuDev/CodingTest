def solution(s):
    answer = [len(s)]
    for n in range(1, int(len(s)/2) + 1):
        words = [s[i: i + n] for i in range(0, len(s), n)]
        res = []
        count = 1
        
        for curr, next in zip(words, words[1:] + ['']):
            if curr == next:
                count += 1
            else:
                res.append([curr, count])
                count = 1
        
        answer.append(sum((len(str(count)) if count > 1 else 0) + len(word) for word, count in res))
    return min(answer)

if __name__ == "__main__":
    print(solution("xababcdcdababcdcd"))