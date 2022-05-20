import sys


def fibona(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    else:
        return fibona(x - 1) + fibona(x - 2)


n = int(sys.stdin.readline().rstrip())
print(fibona(n))
