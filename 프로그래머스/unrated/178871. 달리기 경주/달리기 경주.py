def solution(players, callings):
    answer = []
    rank = dict()
    for ranking,player in enumerate(players):
        rank[player] = ranking
    for i in callings:
        r1, r2 = rank[i] - 1, rank[i]
        rank[players[r1]], rank[players[r2]] = r2, r1
        players[r1], players[r2] = players[r2], players[r1]
    return players