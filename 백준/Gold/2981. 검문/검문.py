import sys
import math

n = int(sys.stdin.readline().rstrip())
nlist = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])
mcount = [nlist[a] - nlist[a - 1] for a in range(1, n)]

result = math.gcd(*mcount)
rlist = []
i = 2
while i <= (math.sqrt(result)) + 1:
    if result % i == 0:
        rlist.append(i)
        if i != (result//i):
            rlist.append(result//i)
    i += 1
rlist.append(result)

for r in sorted(list(set(rlist))):
    print(r, end=' ')