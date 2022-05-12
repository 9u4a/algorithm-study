import sys

a = int(sys.stdin.readline().rstrip())


for _ in range(a):
    oxList = list(sys.stdin.readline().rstrip())
    total = 0
    total2 = 0
    for y in oxList:
        if y == 'O':
            total += 1
            total2 += total
        else:
            total = 0
    print(total2)
