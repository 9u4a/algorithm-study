import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    c, v = map(int, sys.stdin.readline().split())
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(c // v, c % v))
