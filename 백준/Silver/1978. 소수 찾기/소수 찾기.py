import sys

n = int(sys.stdin.readline().rstrip())
listn = list(map(int, sys.stdin.readline().split()))
count = 0
total = 0

for x in listn:
    for y in range(1, x+1):
        if x % y == 0:
            count += 1
    if count == 2:
        total += 1
    count = 0
print(total)
