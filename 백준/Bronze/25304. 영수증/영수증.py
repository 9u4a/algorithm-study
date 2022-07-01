import sys

x = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
result = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result += a * b

if result == x:
    print('Yes')
else:
    print('No')
