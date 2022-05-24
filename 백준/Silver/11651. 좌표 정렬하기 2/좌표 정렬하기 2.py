import sys

n = int(sys.stdin.readline().rstrip())
a = [[' ' for _ in range(2)] for _ in range(n)]

for x in range(n):
    a[x][0], a[x][1] = map(int, sys.stdin.readline().split())
a.sort(key=lambda z: (z[1], z[0]))
for y in range(n):
    print(a[y][0], a[y][1])