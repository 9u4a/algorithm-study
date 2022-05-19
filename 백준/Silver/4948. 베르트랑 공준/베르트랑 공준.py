import sys

n = 1
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    n2 = n * 2 + 1
    total = 0
    count = [1] * n2
    count[1] = 0

    for x in range(2, n2):
        if count[x] == 1:
            for y in range(x * x, n2, x):
                count[y] = 0
    for z in range(n + 1, n2):
        if count[z] == 1:
            total += 1
    print(total)
