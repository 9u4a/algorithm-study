def solution(sizes):
    w = 0
    h = 0
    answer = 0
    for x,y in sizes:
        if y > x:
            x,y = y,x
        w = max(w, x)
        h = max(h, y)
    answer = w * h
    return answer