import sys

s = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    input = sys.stdin.readline().rstrip().split()
    norder = input[0]
    if norder == 'push':
        s.append(input[1])
    elif norder == 'pop':
        print(s.pop() if s else -1)
    elif norder == 'size':
        print(len(s))
    elif norder == 'empty':
        print(0 if s else 1)
    elif norder == 'top':
        print(s[-1] if s else -1)