import sys
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
listn = []
count = 0

for x in range(m, n+1):
    for y in range(1, x+1):
        if x % y == 0:
            count += 1
    if count == 2:
        listn.append(x)
    count = 0
if not listn:
    print(-1)
else:
    print(sum(listn))
    print(min(listn))
