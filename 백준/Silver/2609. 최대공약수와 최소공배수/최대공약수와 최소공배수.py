import sys
import math


def lcm(x, y):
    return x * y // math.gcd(x, y)


a, b = map(int, sys.stdin.readline().split())

print(math.gcd(a, b))
print(lcm(a, b))