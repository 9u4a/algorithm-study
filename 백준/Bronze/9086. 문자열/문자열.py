import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x = sys.stdin.readline().rstrip()
    print(x[0] + x[-1], end='')
    print()
