import sys

a = int(sys.stdin.readline().rstrip())

for i in range(a):
    r, s = map(str, sys.stdin.readline().split())
    p = ""
    for y in s:
        p += y * int(r)
    print(p)