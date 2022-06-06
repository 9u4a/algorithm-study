import sys

a, b = map(int, sys.stdin.readline().split())
seta = set(map(int, sys.stdin.readline().split()))
setb = set(map(int, sys.stdin.readline().split()))

minu1 = len(seta-setb)
minu2 = len(setb-seta)
print(minu1+minu2)