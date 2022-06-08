import sys
import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
