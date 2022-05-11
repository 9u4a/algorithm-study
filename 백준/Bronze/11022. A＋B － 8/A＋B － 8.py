import sys

a = int(sys.stdin.readline().rstrip())
x = ""
for i in range(1, a + 1):
    b, c = map(int, sys.stdin.readline().split())
    x += "Case #%d: %d + %d = %d \n" % (i, b, c, b+c)
print(x)
