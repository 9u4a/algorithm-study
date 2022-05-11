import sys

a = int(sys.stdin.readline().rstrip())
x = ""
for i in range(1, a + 1):
    b, c = map(int, sys.stdin.readline().split())
    x += "Case #" + str(i) + ": " + str(b + c) + "\n"
print(x)
