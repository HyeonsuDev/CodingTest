def solution(id_list, report, k):
    answer = [0] * len(id_list)
    counts = {i : 0 for i in id_list}

    for r in set(report):
        counts[r.split()[1]] += 1

    for r in set(report):
        if counts[r.split()[1]] > k - 1:
            answer[id_list.index(r.split()[0])] += 1

    return answer

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    print(solution(id_list, report, k))


