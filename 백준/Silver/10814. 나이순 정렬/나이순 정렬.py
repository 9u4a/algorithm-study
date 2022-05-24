import sys

n = int(sys.stdin.readline().rstrip())
x = []
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    x.append((int(a), b))
    
x.sort(key=lambda y: y[0])

for z in x:
    print(z[0], z[1])
