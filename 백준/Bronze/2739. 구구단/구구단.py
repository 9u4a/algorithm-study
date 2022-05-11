import sys

c = int(sys.stdin.readline().rstrip())

for i in range(1, 10):
    print(c, "*", i, "=", c*i)
