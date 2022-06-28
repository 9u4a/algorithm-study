import sys

n, k = map(int, sys.stdin.readline().split())


def factorial(x):
    y = 1
    for z in range(2, x + 1):
        y *= z
    return y


print(factorial(n) // (factorial(n-k) * factorial(k)) % 10007)