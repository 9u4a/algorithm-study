import sys

t = int(sys.stdin.readline().rstrip())


def factorial(x):
    y = 1
    for z in range(2, x + 1):
        y *= z
    return y


for _ in range(t):
    k, n = map(int, sys.stdin.readline().split())
    print(factorial(n) // (factorial(n - k) * factorial(k)))
