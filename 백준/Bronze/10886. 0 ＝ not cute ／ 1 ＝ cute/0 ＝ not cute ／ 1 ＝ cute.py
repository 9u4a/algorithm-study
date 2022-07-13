import sys

n = int(sys.stdin.readline().rstrip())
countlist = []
for _ in range(n):
    countlist.append(int(sys.stdin.readline().rstrip()))
zero = countlist.count(0)
one = countlist.count(1)
if zero > one:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
