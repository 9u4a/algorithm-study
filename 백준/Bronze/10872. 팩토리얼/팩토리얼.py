import sys

result = 1


def pacta(x):
    global result
    if x == 0:
        return result
    result *= x
    return pacta(x-1)


n = int(sys.stdin.readline().rstrip())
print(pacta(n))