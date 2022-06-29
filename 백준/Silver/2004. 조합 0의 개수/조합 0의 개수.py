import sys

n, m = map(int, sys.stdin.readline().split())


def count(x, y):
    result = 0
    while x != 0:
        x = x // y
        result += x
    return result


result2 = count(n, 2) - count(n - m, 2) - count(m, 2)
result5 = count(n, 5) - count(n - m, 5) - count(m, 5)

print(min(result2, result5))