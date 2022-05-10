import sys

a, b = map(int, sys.stdin.readline().split())

if b < 45 and a > 0:
    print(a-1, b+15)
elif b >= 45:
    print(a, b-45)
else:
    print(23, b+15)