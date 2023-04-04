import sys

n = int(sys.stdin.readline().rstrip())

q = []

for i in range(n):
    nlist = list(sys.stdin.readline().split())
    if nlist[0] == 'push':
        q.append(nlist[1])

    elif nlist[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.pop(0))

    elif nlist[0] == 'size':
        print(len(q))

    elif nlist[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif nlist[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif nlist[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
