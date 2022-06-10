import sys

a, b = map(int, sys.stdin.readline().split())

result = a * (100-b) / 100

if result >= 100:
    print('0')
else:
    print('1')
