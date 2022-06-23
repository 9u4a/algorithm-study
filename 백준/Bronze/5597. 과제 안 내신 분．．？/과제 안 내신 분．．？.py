import sys

nlist = [i for i in range(0, 31)]
for _ in range(28):
    n = int(sys.stdin.readline().rstrip())
    nlist[n] = 0

for j in range(1, 31):
    if nlist[j] != 0:
        print(nlist[j])
