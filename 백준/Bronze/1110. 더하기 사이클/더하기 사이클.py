import sys

x = int(sys.stdin.readline().rstrip())
count = 0
y = x

while True:
    a = y // 10
    b = y % 10
    y = (b * 10) + (a + b) % 10
    count += 1
    if y == x:
        break

print(count)