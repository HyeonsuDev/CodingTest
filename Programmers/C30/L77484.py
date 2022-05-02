def solution(lottos, win_nums):

    win_count = 0
    zero_count = lottos.count(0)
    rank = [6, 6, 5, 4, 3, 2, 1]

    for i in lottos:
        if i in win_nums:
            win_count += 1

    answer = [rank[zero_count + win_count], rank[win_count]]

    return answer