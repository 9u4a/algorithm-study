import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    yonsei = []
    korea = []
    for i in range(9):
        y, k = map(int, sys.stdin.readline().split())
        yonsei.append(y)
        korea.append(k)
    if sum(korea) == sum(yonsei):
        print('Draw')
    elif sum(korea) > sum(yonsei):
        print('Korea')
    else:
        print('Yonsei')