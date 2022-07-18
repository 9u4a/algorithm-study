import sys

s = sys.stdin.readline().rstrip()

reverse = s[::-1]

if s == reverse:
    print(1)
else:
    print(0)
