import sys

n = int(sys.stdin.readline().rstrip())
count = 0
if n == 1:
    count = 1
else:
    i = 1
    d = 6
    count = 2
    while True:
        if i < n <= i + d:
            break
        else:
            i += d
            d += 6
            count += 1
print(count)