import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    floor0 = [x for x in range(1, n + 1)]
    for y in range(k):
        for z in range(1, n):
            floor0[z] += floor0[z-1]
    print(floor0[-1])