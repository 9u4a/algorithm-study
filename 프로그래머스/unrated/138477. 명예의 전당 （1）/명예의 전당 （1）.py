def solution(k, score):
    answer = []
    rank = []
    for i in score:
        if len(rank) < k:
            rank.append(i)
        elif min(rank) < i:
            rank.remove(min(rank))
            rank.append(i)
        answer.append(min(rank))
    return answer