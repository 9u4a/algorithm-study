import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

x = [x1, x2, x3]
y = [y1, y2, y3]
resx = resy = 0

for z in range(3):
    countx = x.count(x[z])
    county = y.count(y[z])
    if countx == 1:
        resx = x[z]
    if county == 1:
        resy = y[z]

print(resx, resy)
