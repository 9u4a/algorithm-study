import sys

n = int(sys.stdin.readline().rstrip())
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1

print('Q1: {}'.format(Q1))
print('Q2: {}'.format(Q2))
print('Q3: {}'.format(Q3))
print('Q4: {}'.format(Q4))
print('AXIS: {}'.format(AXIS))
