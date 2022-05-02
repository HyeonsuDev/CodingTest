from datetime import datetime

def solution(lines):
    answer = 0
    
    memo = {}
    k = []
    for l in lines:
        s1, s2, t = l.split(" ")
        s = s1 + " " + s2
        stmp = datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f").timestamp()
        k.append((round(stmp, 3), round(float(t[:-1]), 3)))

    
    for s1, t1 in k:
        start = round(s1 - t1 + 0.001, 3)
        if start not in memo:
            memo[start] = 0

        if s1 not in memo:
            memo[s1] = 0

        for s2, t2 in k:
            if start <= s2:
                memo[start] += 1

            if s1 >= round((s2 - t2 + 0.001), 3):
                memo[s1] += 1

    answer = min(memo.values())
    return answer

if __name__ == "__main__":
    print(solution([
        "2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"
    ]))