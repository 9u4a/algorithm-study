import sys

n = int(sys.stdin.readline().rstrip())
listx = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    listx.append((x, y))

for i in listx:
    count = 1
    for j in listx:
        if j[0] > i[0] and j[1] > i[1]:
            count += 1
    print(count, end=" ")
