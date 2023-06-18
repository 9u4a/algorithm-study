def solution(n, m, section):
    paint = section[0] -1
    answer = 0
    for s in section:
        if s > paint:
            paint = s + m-1
            answer += 1
    return answer