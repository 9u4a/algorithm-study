import sys

a = int(sys.stdin.readline().rstrip())
x = ""
for i in range(0, a):
    b, c = map(int, sys.stdin.readline().split())
    x += str(b + c) + "\n"
print(x)
