def solution(price, money, count):
    answer = 0
    total = count * (count + 1) * price / 2
    return max(answer, total - money)