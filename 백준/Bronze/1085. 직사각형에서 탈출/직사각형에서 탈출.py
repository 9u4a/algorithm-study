import sys

x, y, w, h = map(int, sys.stdin.readline().split())
countlist = []

countlist.append(w-x)
countlist.append(x)
countlist.append(h-y)
countlist.append(y)

print(min(countlist))
