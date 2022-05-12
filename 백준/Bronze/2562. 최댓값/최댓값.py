import sys

x = []
for i in range(9):
    x += [int(sys.stdin.readline().rstrip())]

a = max(x)
b = x.index(a) + 1

print(str(a)+"\n"+str(b))
