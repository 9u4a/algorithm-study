import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)

for i in range(n, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
