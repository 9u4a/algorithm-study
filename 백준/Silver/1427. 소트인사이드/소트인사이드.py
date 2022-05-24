import sys

n = list(map(int, sys.stdin.readline().rstrip()))
n.sort()
n.reverse()
print("".join(str(i) for i in n))