import sys


def plist(n):
    count = [1] * n
    count[1] = 0
    for x in range(2, n):
        if count[x] == 1:
            for y in range(x * x, n, x):
                count[y] = 0
    return count


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n2 = int(sys.stdin.readline().rstrip())
    prList = plist(n2)

    for a in range(n2 // 2, 1, -1):
        if prList[n2 - a] == 1 and prList[a] == 1:
            print(a, n2 - a)
            break
