import sys

intlist = list(map(int, sys.stdin.readline().split()))
intlist.sort()
print(intlist[1])
