import sys

a, b = sys.stdin.readline().split()

a = list(a)
b = list(b)

a.reverse()
b.reverse()

if int("".join(a)) > int("".join(b)):
    print("".join(a))
else:
    print("".join(b))
