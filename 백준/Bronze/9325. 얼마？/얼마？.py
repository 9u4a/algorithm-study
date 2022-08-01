import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    s = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    price = 0
    for _ in range(n):
        q, p = map(int, sys.stdin.readline().split())
        price += q * p
    print(price + s)
