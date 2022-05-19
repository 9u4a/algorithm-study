import sys
m, n = map(int, sys.stdin.readline().split())

count = [1] * (n+1)
count[1] = 0
for x in range(2, n+1):
    if count[x] == 1:
        for y in range(x*x, n+1, x):
            count[y] = 0

for z in range(m, n+1):
    if count[z] == 1:
        print(z)
