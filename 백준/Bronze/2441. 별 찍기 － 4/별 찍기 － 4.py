import sys

n = int(sys.stdin.readline().rstrip())

for i in range(0, n):
    print(' '*i+'*'*(n-i))
