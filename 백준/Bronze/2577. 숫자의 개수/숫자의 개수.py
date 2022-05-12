import sys

x = 1
for i in range(3):
    a = int(sys.stdin.readline().rstrip())
    x *= a

y = str(x)
list(y)
for e in range(0, 10):
    print(y.count(str(e)))
