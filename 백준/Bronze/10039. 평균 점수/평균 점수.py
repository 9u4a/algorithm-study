import sys

total = []
for _ in range(5):
    point = int(sys.stdin.readline().rstrip())
    if point < 40:
        point = 40
    total.append(point)

print(sum(total)//5)
