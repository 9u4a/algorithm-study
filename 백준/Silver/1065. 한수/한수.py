import sys


def solve(n):
    count = 0
    for i in range(1, n + 1):
        nlist = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif nlist[0] - nlist[1] == nlist[1] - nlist[2]:
            count += 1
    return count


x = int(sys.stdin.readline().rstrip())
print(solve(x))
