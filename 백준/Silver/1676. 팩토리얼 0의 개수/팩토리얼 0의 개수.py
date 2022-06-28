import sys


def find0(x):
    y = 1
    for z in range(2, x + 1):
        y *= z
    factorial = str(y)[::-1]

    for i in range(len(factorial)):
        if factorial[i] != '0':
            return factorial[:i].count('0')


n = int(sys.stdin.readline().rstrip())

print(find0(n))