import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    nlist = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    count = 0
    error = False

    if n == 0:
        nlist = deque()

    for i in p:
        if i == 'R':
            count += 1
        elif i == 'D':
            if len(nlist) == 0:
                print("error")
                error = True
                break
            elif count % 2 == 0:
                nlist.popleft()
            else:
                nlist.pop()

    if not error:
        if count % 2 == 0:
            print("[" + ",".join(nlist) + "]")
        else:
            nlist.reverse()
            print("[" + ",".join(nlist) + "]")



