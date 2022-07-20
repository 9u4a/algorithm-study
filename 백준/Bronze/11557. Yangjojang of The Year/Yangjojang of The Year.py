import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    result = ''
    maxcount = 0
    for _ in range(n):
        s, count = sys.stdin.readline().split()
        if maxcount < int(count):
            result = s
            maxcount = int(count)
    print(result)
