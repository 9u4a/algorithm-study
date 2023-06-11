def solution(a, b, n):
    answer = 0
    while n >= a:
        result = n // a * b
        n = n % a + result
        answer += result
    return answer